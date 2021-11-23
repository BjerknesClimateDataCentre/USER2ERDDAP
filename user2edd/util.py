# Stdlib imports
import re
import warnings

# Third-party app imports
from validate_email import validate_email

# Imports from my apps


def reverse_dict(dict_):
    """reverse dictionary

    Example:
    >>> d = {'iso': ['a', 'b'], 'iso2': ['b']}
    >>> reverse_dict(d)
    {'a': ['iso'], 'b': ['iso', 'iso2']}
    """
    _ = {}
    for k, v in dict_.items():
        for vv in list(v):
            _.setdefault(vv, []).append(k)

    return _


def urlify(s):
    """
    Replacing spaces, and other URL-hostile characters
    like question marks, apostrophes, exclamation points, etc.

    Example:
    >>> s = 'iso met'
    iso_met
    >>> s = 'isomet?'
    'isomet'
    """
    # Remove all non-word characters (everything except numbers and letters)
    s = re.sub(r"[^\w\s]", "", s)

    # Replace all runs of whitespace with a single dash
    s = re.sub(r"\s+", "_", s)

    return s


def camelCase(word_, sep=" "):
    """rewrite with camelCase format

    >>> word = ["Hello", "World", "Python", "Programming"]
    >>> camelCase(word)
    'helloWorldPythonProgramming'
    >>> word = 'toto_25_tutu'
    >>> camelCase(word, sep='_')
    'toto25Tutu'
    >>> camelCase(word)
    'toto_25_tutu'
    """
    if isinstance(word_, list):
        words = word_
    else:
        words = word_.split(sep=sep)

    s = "".join(word[0].upper() + word[1:].lower() for word in words)
    return s[0].lower() + s[1:]


def email_is_valid(email_, smtp_=False):
    """
    check if an email is valid, not blacklisted, properly formatted and really exists.

    Note: do not check whether the email actually exists by initiating an SMTP conversation, as it seems to fail.
    """
    is_valid = validate_email(email_address=email_, check_smtp=smtp_)
    if not is_valid:
        # warnings.warn(f"Invalid email: {email_}")
        raise ValueError(f"Invalid email: {email_}")
