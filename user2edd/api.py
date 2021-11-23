"""Application script for user2edd.
module: api.py
"""
# Stdlib imports
import logging

# Third-party app imports
# Imports from my apps
import user2edd.parameters as parameters
import user2edd.setupcfg as setupcfg
import user2edd.timing
import user2edd.xml4Erddap as x4edd


def main(args={}):
    """ """
    print(f"Running {__file__} \n...")
    # set up logger, paths, ...
    setupcfg.main(args)
    _logger = logging.getLogger(__name__)

    # load and check parameters
    param = parameters.main()

    try:
        # concatenate header.xml dataset.XXX.xml footer.xml into local datasets.xml
        dsxmlout = x4edd.concatenate()
        _logger.info(
            "change/add metadata on datasets.xml file, considering metadata from ICOS CP"
        )
    except Exception:
        _logger.exception(
            "Something goes wrong when concatenate xml files into local datasets.xml"
        )
        raise  # Throw exception again so calling code knows it happened

    try:
        _logger.info("change/add attributes into local datasets.xml")
        x4edd.addUserAndGroup(dsxmlout, param)
        _logger.info("replace ERDDAP datasets.xml file with the new one")
        x4edd.replaceXmlBy(dsxmlout)

    except Exception:
        _logger.exception(
            "Something goes wrong when changing/adding attributes into ERDDAP datasets.xml"
        )
        raise  # Throw exception again so calling code knows it happened


if __name__ == "__main__":
    try:
        main()
    except Exception:
        logging.exception("Something goes wrong!!!")
        raise  # Throw exception again so calling code knows it happened
