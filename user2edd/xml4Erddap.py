"""
module: xml4Erddap.py
"""
# Stdlib imports
import logging
from pathlib import Path
import re
import warnings

# Third-party app imports
import lxml.etree as etree

# Imports from my apps
import user2edd.setupcfg as setupcfg
from user2edd.util import reverse_dict

# --- module's variable ------------------------
# load logger
_logger = logging.getLogger(__name__)


def concatenate():
    """concatenate header.xml dataset.XXX.xml footer.xml into local datasets.xml

    >>> xmlout = concatenate()
    concatenate in .../datasets.xml
    \t.../header.xml
    ...
    \t.../footer.xml
    >>> xmlout.__str__()
    '.../datasets.xml'
    """
    dsxmlout = setupcfg.datasetXmlPath / "datasets.xml"
    pattern = f".*({'|'.join(setupcfg.exclude.replace(' ','').split(','))}).*"
    _logger.debug(f"concatenate in {dsxmlout}")
    with dsxmlout.open("w") as fp:
        # add header
        header = setupcfg.user2eddPath / "dataset" / "header.xml"
        _logger.debug("\t{}".format(header))
        fp.write(header.read_text())
        # add single dataset
        for ff in setupcfg.datasetXmlPath.glob("**/dataset.*.xml"):
            if not re.match(pattern, str(ff)):
                _logger.debug("\t{}".format(ff))
                fp.write(ff.read_text(encoding="unicode_escape"))
        # add footer
        footer = setupcfg.user2eddPath / "dataset" / "footer.xml"
        _logger.debug("\t{}".format(footer))
        fp.write(footer.read_text())

    return dsxmlout


def addUserAndGroup(ds_, dict_, out_=None):
    """
    :param ds_: str
       input filename
    :param dict_: dictionary
       users and groups dictionary
    :param out_: str
       output filename, optional
    """
    if not isinstance(ds_, Path):
        ds_ = Path(ds_)

    if not isinstance(dict_, dict):
        raise TypeError(f"Invalid type value, dict_ -{dict_}- must be dictionary")

    if out_ is not None and not isinstance(out_, str):
        raise TypeError(f"Invalid type value, out -{out_}- must be string")

    if not ds_.is_file():
        raise FileExistsError(f"File {ds_} does not exist.")
    else:
        _logger.info(f"tree: {ds_}")

    # keep CDATA as it is
    parser = etree.XMLParser(
        strip_cdata=False,
        encoding="ISO-8859-1",
    )

    print(ds_)
    tree = etree.parse(str(ds_), parser)
    root = tree.getroot()

    # prevent creation of self-closing tags
    for node in root.iter():
        if node.text is None:
            node.text = ""

    # inset users list
    subtag = root.find("subscriptionEmailBlacklist")
    for user, groups in reverse_dict(dict_["google_users"]).items():
        usertag = etree.Element(
            "user",
            username=f"{user}",
            roles=", ".join(f"{r}" for r in groups),
            # roles=", ".join(f'"{r}"' for r in groups),
        )
        subtag.addnext(usertag)  # Add usertag as a following sibling of subtag
        subtag.tail = "\n"  # Add linebreak before usertag
        subtag = usertag

    # insert accesible groups
    for dsID, groups in reverse_dict(dict_["dataset_ids"]).items():
        datasettag = root.find(f".//dataset[@datasetID='{dsID}']")
        if datasettag is not None:
            grouptag = datasettag.find("accessibleTo")
            if grouptag is not None:
                if grouptag.text == "[anyoneLoggedIn]":
                    grouptag.text = ""
                else:
                    grouptag.text += ", "
            else:
                grouptag = etree.Element("accessibleTo")

            grouptag.text += ", ".join(f"{r}" for r in groups)
            datasettag.insert(
                0, grouptag
            )  # Add grouptag as the first child (index 0) of the dataset element
            grouptag.tail = "\n    "  # Add linebreak after grouptag
        else:
            warnings.warn(f"No dataset with datasetID: {dsID} in {ds_}")

    # write xml output
    if out_ is not None:
        dsout = out_
    else:
        dsout = ds_

    tree.write(
        str(dsout), pretty_print=True, encoding="ISO-8859-1", xml_declaration=True
    )


def replaceXmlBy(dsxmlout):
    """overwrite erddap datasets.xml with the new one
    :param dsxmlout:
    """
    # remove erddap datasets.xml and create hard link to the new one
    dsxml = setupcfg.erddapContentDir / "datasets.xml"
    if dsxml.is_file():  # and not dsxml.is_symlink():
        dsxml.unlink()

    _logger.info(f"create hard link to: {dsxmlout}")
    dsxmlout.link_to(dsxml)
