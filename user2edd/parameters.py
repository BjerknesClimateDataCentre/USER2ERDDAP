"""
module: parameters.py
"""
# Stdlib imports
import logging
from pprint import pformat

# Third-party app imports
import yaml

# Imports from my apps
import user2edd.setupcfg as setupcfg
import user2edd.util as util

# --- module's variable ------------------------
# load logger
_logger = logging.getLogger(__name__)


# ----------------------------------------------
def _check_param_dataset_ids(dict_):
    """ """
    # default empty dictionary
    _ = {}

    # check value are list
    for key, val in dict_.items():
        # change key format
        key = util.camelCase(util.urlify(key), sep="_")
        #
        if isinstance(val, str):
            val = [val]
        else:
            val = list(val)

        _[key] = val

    return _


def _check_param_google_users(dict_):
    """ """
    # default empty dictionary
    _ = {}

    # check value are list
    for key, val in dict_.items():
        # change key format
        key = util.camelCase(util.urlify(key), sep="_")
        # check emails
        if isinstance(val, str):
            val = [val]
        else:
            val = list(val)

        for email in val:
            util.email_is_valid(email)

        _[key] = val

    return _


def _check_param(dict_):
    """
    check dictionary elements and reformat if need be

    :return: dictionary reformat
    """
    # default empty dictionary
    _ = {}

    if "google_users" in dict_:
        _["google_users"] = _check_param_google_users(dict_["google_users"])
    else:
        _logger.exception(f"No key 'google_users' in yaml file {setupcfg.extraParam}")
        raise KeyError

    if "dataset_ids" in dict_:
        _["dataset_ids"] = _check_param_dataset_ids(dict_["dataset_ids"])
    else:
        _logger.exception(f"No key 'dataset_ids' in yaml file {setupcfg.extraParam}")
        raise KeyError

    return _


def show(param_):
    """ """
    print(f"parameters:\n {pformat(param_)}")


def main():
    """ """
    try:
        # init
        param = {}
        # read parameters configuration file yaml
        with open(setupcfg.extraParam, "r") as stream:
            try:
                param = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                _logger.exception(exc)

        # check parameters file
        return _check_param(param)

    except Exception:
        _logger.exception(
            f"Something goes wrong when loading extra parameters file -{setupcfg.extraParam}-."
        )
        raise  # Throw exception again so calling code knows it happened


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    try:
        main()
    except Exception:
        logging.exception("Something goes wrong!!!")
        raise  # Throw exception again so calling code knows it happened
