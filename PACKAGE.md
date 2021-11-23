# Package info

we use **setuptools** to create this package

## How to set up/update  package library

## How to install package
$ python3 -m pip install path/to/package/dist/icp2edd.SOME_RELEASE.tar.gz

## How to install package in development mode
$ pip(3) install -e path/to/package

## How to install one of github hosted repo's specific tag
### using git clone

$ git clone -b { tag name } --single-branch { repo name } .  

> --single-branch flag prevents fetching all the branches in the cloned repository

### using pip
$ pip(3) install -e git+https://github.com/{ username }/{ repo name }.git@{ tag name }#egg={ desired egg name }

> for 'egg name', use the contents of project-name.egg-info/top_level.txt

### exemple, for tag 0.7.0
pip install git+https://github.com/BjerknesClimateDataCentre/USER2ERDDAP.git@0.7.0#egg=user2edd

## Version

user2edd --version

## Semantic Version (Sem-Ver):
 Given a version number MAJOR.MINOR.PATCH, increment the:
 - MAJOR version when you make incompatible API changes,
 - MINOR version when you add functionality in a backwards-compatible manner, and
 - PATCH version when you make backwards-compatible bug fixes.

## Change version: bump2version
```python
bump2version part
```
`part`:
    The part of the version to increase [`major`, `minor`, `patch`]

> configuration file in `setup.cfg`

see also [bump2version](https://github.com/c4urself/bump2version)