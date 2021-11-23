# Stdlib imports
import pytest
from pprint import pformat

# Third-party app imports
# Imports from my apps
from user2edd import parameters
from user2edd import setupcfg


def test__check_param_dataset_ids():
    """
    GIVEN a dictionary
    WHEN  applying _check_param_dataset_ids
    THEN  return a dictionary with key in camel case format
     and  value in a list
    """
    A = {"aa bbb": "aa"}
    expected = {"aaBbb": ["aa"]}
    assert expected == parameters._check_param_dataset_ids(A)

    A = {"aaa@bbb": ["a", "b"]}
    expected = {"aaabbb": ["a", "b"]}
    assert expected == parameters._check_param_dataset_ids(A)

    A = {"aaa_bbb": ["a", "b"]}
    expected = {"aaaBbb": ["a", "b"]}
    assert expected == parameters._check_param_dataset_ids(A)


def test__check_param_google_users():
    """
    GIVEN a dictionary
     with value an email
    WHEN  applying function
    THEN  return dictionary
     with key reformat to camel case, urlified
     and  value as list
    """
    A = {"aaa_bbb": "user.name@something.com"}
    expected = {"aaaBbb": ["user.name@something.com"]}
    assert expected == parameters._check_param_google_users(A)
    A = {"aaa!bbb": ["user.name@something.com", "another@elsewhere.org"]}
    expected = {"aaabbb": ["user.name@something.com", "another@elsewhere.org"]}
    assert expected == parameters._check_param_google_users(A)


def test__check_param_no_key_google_users():
    """
    GIVEN a dictionary
     with no key 'google_users'
    WHEN  running function
    THEN  raise an Exception
     and  write error message in loggers
    """
    setupcfg.extraParam = "template"
    A = {"a": "b"}
    with pytest.raises(KeyError) as execinfo:
        parameters._check_param(A)
    # check error message
    # assert str(execinfo.value).startswith("No key 'google_users'")


def test__check_param_no_key_dataset_ids():
    """
    GIVEN a dictionary
     with no key 'dataset_ids'
    WHEN  running function
    THEN  raise an Exception
     and  write error message in loggers
    """
    setupcfg.extraParam = "template"
    email_ = "user@uib.no"
    A = {"google_users": {"b": email_}, "a": {"a": "a"}}
    with pytest.raises(KeyError) as execinfo:
        parameters._check_param(A)
    # check error message
    # assert str(execinfo.value).startswith("No key 'dataset_ids'")


def test__check_param_raises_no_exception():
    """
    GIVEN a valid dictionary
     with keys 'google_users' and 'dataset_ids'
     and  value
    WHEN  running function
    THEN  raise no Exception
    """
    email_ = "julien.paul@uib.no"
    A = {"google_users": {"b": email_}, "dataset_ids": {"b": "aa"}}
    try:
        parameters._check_param(A)
    except Exception as exc:
        assert False, f"parameters._check_param({A}) raised an exception {exc}"


@pytest.mark.skip(reason="not implemented yet")
def test_show(capsys):
    """
    GIVEN a dictionary
    WHEN  running function
    THEN  print dictionary
    """
    email_ = "julien.paul@uib.no"
    A = {"google_users": {"b": email_}, "dataset_ids": {"b": "aa"}}
    parameters.show(A)
    captured = capsys.readouterr()
    assert captured.err == ""
    assert captured.out == f"parameters:\n {pformat(A)}"


def test_main_no_file():
    """
    GIVEN a wrong filename
    WHEN  running main
    THEN  should raise Exception
    """
    setupcfg.extraParam = "template"
    with pytest.raises(FileNotFoundError) as execinfo:
        parameters.main()
    # check error message
    assert str(execinfo.value).startswith("[Errno 2] No such file or directory")
    # "Something goes wrong when loading extra parameters"


def test__check_main_raises_no_exception():
    """
    GIVEN a valid input yaml file
    WHEN  running main
    THEN  raise no Exception
    """
    setupcfg.main()
    try:
        parameters.main()
    except Exception as exc:
        assert False, f"parameters.main() raised an exception {exc}"
