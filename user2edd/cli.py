"""Console script for user2edd.
module: cli.py
"""
# Stdlib imports
import argparse
import sys

# Third-party app imports
# Imports from my apps
from user2edd import api


def _parse():
    """set up parameter from command line arguments"""
    # define parser
    parser = argparse.ArgumentParser(prog="icp2edd", description="blabla")

    # positional arguments
    # parser.add_argument("name", type=str, help="file name")
    # optional arguments
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="print status messages to stdout",
        dest="log.verbose",
    )
    parser.add_argument(
        "--log_level",
        type=str,
        choices=["debug", "info", "warning", "error", "critical"],
        help="stdout logger level",
        dest="log.level",
    )
    parser.add_argument(
        "--log_filename", type=str, help="logger filename", dest="log.filename"
    )
    parser.add_argument(
        "--log_path",
        type=str,
        help="logger path, where log will be stored",
        dest="paths.log",
    )
    parser.add_argument(
        "--param",
        type=str,
        help="parameters configuration file",
        dest="extra.parameters",
    )
    #
    parser.add_argument(
        "--arguments",
        action="store_true",
        help="print arguments value (from config file and/or inline argument) and exit",
        dest="arguments",
    )
    parser.add_argument(
        "--version",
        action="store_true",
        help="print release version and exit",
        dest="version",
    )

    # parse arguments
    args = parser.parse_args()

    # TODO check and reformat args
    return args


def main():
    """Console script for user2edd."""
    # read command line arguments
    args = _parse()

    api.main(args)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
