#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

requirements = []

test_requirements = [
    "pytest>=3",
]

setup(
    author="Julien Paul",
    author_email="julien.paul@uib.no",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    description="handle ERDDAP's user and group.",
    entry_points={
        "console_scripts": [
            "user2edd=user2edd.cli:main",
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="user2edd",
    name="user2edd",
    packages=find_packages(include=["user2edd", "user2edd.*"]),
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/julienpaul/user2edd",
    version="version='0.2.0'",
    zip_safe=False,
)
