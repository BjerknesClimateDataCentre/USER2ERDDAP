# Stdlib imports
import pytest

# Third-party app imports
# Imports from my apps
from user2edd import util


def test_reverse_dict():
    """
    GIVEN a dictionary A
    WHEN  running reverse_dict
    THEN  should return a dictionary with values of A as key, and
    """
    A = {"x": ["a", "b"], "Y": ["b"]}
    expected = {"a": ["x"], "b": ["x", "Y"]}
    assert expected == util.reverse_dict(A)

    B = {"x": ["a", "b"], "Y": "b"}
    expected = {"a": ["x"], "b": ["x", "Y"]}
    assert expected == util.reverse_dict(B)


def test_urlify():
    """
    GIVEN a string
    WHEN  applying urlify
    THEN  must return a string where:
        space have been replaced by underscore
        URL-hostile characters [?'!...] should have been removed
    """
    string = "iso met"
    assert util.urlify(string) == "iso_met"
    string = "iso-met"
    assert util.urlify(string) == "isomet"
    string = "isomet?"
    assert util.urlify(string) == "isomet"
    string = "is@met"
    assert util.urlify(string) == "ismet"


def camelCase():
    """
    GIVEN a list of world
    WHEN  applying camelCase
    THEN  must return one word with camel case format
    """
    words = ["Hello", "World", "Python", "Programming"]
    assert util.camelCase(words) == "helloWorldPythonProgramming"
    words = ["hello", "world", "python", "programming"]
    assert util.camelCase(words) == "helloWorldPythonProgramming"


def camelCase_separator():
    """
    GIVEN a word with underscore
    WHEN  specifying sep='_'
    THEN  must return one word without underscore and camel case format
    """
    word = "toto_25_tutu"
    assert util.camelCase(word, sep="_") == "toto25Tutu"


def camelCase_no_separator():
    """
    GIVEN a word with underscore
    WHEN  not specifying separator
    THEN  must return the same words
    """
    word = "toto_25_tutu"
    assert util.camelCase(word, sep="_") == "toto_25_tutu"


def test_email_is_valid_raises_no_exception():
    """
    GIVEN a valid email
    WHEN  checking email format
    THEN  raise no Exception
    """
    email_ = "julien.paul@uib.no"
    try:
        util.email_is_valid(email_)
    except Exception as exc:
        assert False, f"util.email_is_valid({email_}) raised an exception {exc}"


def test_email_is_valid_raises_exception():
    """
    GIVEN an invalid email
    WHEN  checking email format
    THEN  should raise ValueError
    """
    email_ = "julien.pauluib.no"
    with pytest.raises(ValueError) as execinfo:
        util.email_is_valid(email_)
    # check error message
    assert str(execinfo.value).startswith("Invalid email")


@pytest.mark.skip(reason="not working yet")
def test_email_is_valid_smtp_success():
    """
    GIVEN a valid email
    WHEN  checking format and SMTP
    THEN  should return True
    """
    email_ = "julien.paul@uib.no"
    assert util.email_is_valid(email_, smtp_=True)
