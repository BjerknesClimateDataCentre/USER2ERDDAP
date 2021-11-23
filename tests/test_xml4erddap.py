# Stdlib imports
import pytest

# Third-party app imports
# Imports from my apps
from user2edd import xml4Erddap as x4edd
from user2edd import setupcfg


def test_concatenate_raises_no_exception():
    """
    GIVEN a path to a header.xml file
      and a footer.xml
      and a
    WHEN  running
    THEN  create a datasets.xml file
    """
    setupcfg.main()
    try:
        x4edd.concatenate()
    except Exception as exc:
        assert False, f"parameters.main() raised an exception {exc}"
    # """concatenate header.xml dataset.XXX.xml footer.xml into local datasets.xml

    # >>> xmlout = concatenate()
    # concatenate in .../datasets.xml
    # \t.../header.xml
    # ...
    # \t.../footer.xml
    # >>> xmlout.__str__()
    # '.../datasets.xml'
    # """
    # dsxmlout = setupcfg.datasetXmlPath / "datasets.xml"
    # _logger.debug(f"concatenate in {dsxmlout}")
    # with dsxmlout.open("w") as fp:
    #     # add header
    #     header = setupcfg.user2eddPath / "dataset" / "header.xml"
    #     _logger.debug("\t{}".format(header))
    #     fp.write(header.read_text())
    #     # add single dataset
    #     for ff in setupcfg.datasetXmlPath.glob("**/dataset.*.xml"):
    #         _logger.debug("\t{}".format(ff))
    #         fp.write(ff.read_text(encoding="unicode_escape"))
    #     # add footer
    #     footer = setupcfg.user2eddPath / "dataset" / "footer.xml"
    #     _logger.debug("\t{}".format(footer))
    #     fp.write(footer.read_text())

    # return dsxmlout
