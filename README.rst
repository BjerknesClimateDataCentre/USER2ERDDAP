========
USER2EDD
========


.. image:: https://img.shields.io/pypi/v/user2edd.svg
        :target: https://pypi.python.org/pypi/user2edd

.. image:: https://img.shields.io/travis/julienpaul/user2edd.svg
        :target: https://travis-ci.com/julienpaul/user2edd

.. image:: https://readthedocs.org/projects/user2edd/badge/?version=latest
        :target: https://user2edd.readthedocs.io/en/latest/?version=latest
        :alt: Documentation Status




Python package to handle ERDDAP user permission.


* Free software: MIT license
* Documentation: https://user2edd.readthedocs.io.

Install package
---------------
see [PACKAGE.md](PACKAGE.md)

Run package
-----------

## To run 'package' from terminal

.. code-block:: shell

    $ user2edd

### To get help/usage message

.. code-block:: shell

    $ user2edd --help

Configuration file
------------------

This file contains configuration parameters
> **NOTE:** arguments overwrite value in configuration file.

Put your own configuration file in `~/.config/user2edd/config.yaml`

.. code-block:: shell

    # This is the default config file for user2edd
    paths:
        # erddap: path of the main ERDDAP repository [tomcat]
        erddap: '/home/jpa029/erddap.localhost/apache-tomcat'
        # webinf: path to the 'WEB-INF' repository
        webinf: '/home/jpa029/erddap.localhost/apache-tomcat/webapps/ROOT/WEB-INF'
        # dataset: path where store file from each dataset
        dataset:
            # path where store xml file from BCDC for each dataset
            xml: '/home/jpa029/erddap.localhost/Dataset/xml'
            # exclude subdirectories ex: 'archive, useless'
            exclude: 'archive'
        # log: path where store output log file
        log: '/home/jpa029/Data/USER2ERDDAP/log'

    log:
        # filename: logger filename [default debug.log]
        filename:
        # Below, apply only on standard output log
        # verbose: activate verbose mode [True|False]
        verbose: False
        # level: log level [DEBUG, INFO, WARN, ERROR, CRITICAL]
        level: 'INFO'

    extra:
        # parameters: extra parameters configuration file for user2edd
        parameters: 'parameters.yaml'


Parameters files
----------------
This file contains parameters to run

.. code-block:: python

    # This is the parameters file for user2edd

    # google_users:   # list of group and associated users
    #   <group name>: [
    #      # list of users' member of this group
    #      <user x>, 
    #      <user y>,
    #      ]
    # dataset_ids:  # list of group and associated dataset_ids
    #   <group name>: [ 
    #      # list of dataset_ids only accesible to this groups' members
    #      <dataset_id x>, 
    #      <dataset_id y>,
    #      ] 

    google_users:
       isomet: [ 
            user1.name1@something.no,
            user2.name2@otherthing.uk,
            ]

    dataset_ids:
       isomet: [
            'xxxx',
            'yyyy',
            ] 

Tests
-----
see [HERE](tests/README.md)

Schedule job
------------

.. code-block:: shell

    $ crontab -e  

    
.. code-block:: shell

    # crontab -e
    SHELL=/bin/bash
    MAILTO=jpa029@uib.no
    
    # Example of job definition:
    # m h dom mon dow   command
    
    # * * * * *  command to execute
    # ┬ ┬ ┬ ┬ ┬
    # │ │ │ │ │
    # │ │ │ │ │
    # │ │ │ │ └───── day of week (0 - 6) (Sunday=0 or 7) OR sun,mon,tue,wed,thu,fri,sat
    # │ │ │ └────────── month (1 - 12)
    # │ │ └─────────────── day of month (1 - 31)
    # │ └──────────────────── hour (0 - 23)
    # └───────────────────────── min (0 - 59)
    
    # For details see man 4 crontabs
    
    # daily update (at 00:30) of users and datasets' permission on ERDDAP server
    30 00 * * * user2edd

Features
--------

* TODO

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
