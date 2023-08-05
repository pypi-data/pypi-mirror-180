.. These are examples of badges you might want to add to your README:
   please update the URLs accordingly

    .. image:: https://api.cirrus-ci.com/github/<USER>/mbsim.svg?branch=main
        :alt: Built Status
        :target: https://cirrus-ci.com/github/<USER>/mbsim
    .. image:: https://readthedocs.org/projects/mbsim/badge/?version=latest
        :alt: ReadTheDocs
        :target: https://mbsim.readthedocs.io/en/stable/
    .. image:: https://img.shields.io/coveralls/github/<USER>/mbsim/main.svg
        :alt: Coveralls
        :target: https://coveralls.io/r/<USER>/mbsim
    .. image:: https://img.shields.io/pypi/v/mbsim.svg
        :alt: PyPI-Server
        :target: https://pypi.org/project/mbsim/
    .. image:: https://img.shields.io/conda/vn/conda-forge/mbsim.svg
        :alt: Conda-Forge
        :target: https://anaconda.org/conda-forge/mbsim
    .. image:: https://pepy.tech/badge/mbsim/month
        :alt: Monthly Downloads
        :target: https://pepy.tech/project/mbsim
    .. image:: https://img.shields.io/twitter/url/http/shields.io.svg?style=social&label=Twitter
        :alt: Twitter
        :target: https://twitter.com/mbsim

.. image:: https://img.shields.io/badge/-PyScaffold-005CA0?logo=pyscaffold
    :alt: Project generated with PyScaffold
    :target: https://pyscaffold.org/

.. image:: https://gitlab.com/nee2c/mbsim/badges/master/pipeline.svg

.. image:: https://readthedocs.org/projects/mbsim/badge/?version=latest
    :target: https://mbsim.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status

|

=====
mbsim
=====


    A Modbus Simulator


This is the command line to to control mbsim.  There is a addon system for mbsim.

Installation
============

To install mbsim you can install from
`gitlab package registry <https://gitlab.com/nee2c/mbsim/-/packages/>`_

or

use pip ``pip install mbsim``

Usages
======

::

   mbsim [-h] [-l {DEBUG,INFO,ERROR,WARNING,CRITICAL}] {sim,ui} ...

   mbsim ui {ui1,ui2,...} # a ui addon need to be installed for this command

   mbsim sim [-h] {tcp,udp,rtu} ...

   mbsim sim tcp [-h] [-a SIM_ADDRESS] [-p SIM_PORT]

   mbsim sim udp [-h] [-a SIM_ADDRESS] [-p SIM_PORT]

   mbsim sim rtu [-h] [-b SIM_BUAD] [--bytesize SIM_BYTE]
     [-s SIM_STOPBITS] [-p {N,O,E}] [-t SIM_TIMEOUT]
     [-x {0,1}] [-r {0,1}]
     [path]


Addons
======

mbsim looks for the following entry points under the group mbsim_command and mbsim_ui.

Under mbsim_ui will call the function to start the ui

Under mbsim_command will call the function and pass parser from argparse and expect a function to be returned that is
expecting a Namespace from argparse

For examples see `sim`_ and `ui`_

.. _sim: https://gitlab.com/nee2c/mbsim/-/blob/master/src/mbsim/sim.py
.. _ui: https://gitlab.com/nee2c/mbsim/-/blob/master/src/mbsim/ui.py

.. _pyscaffold-notes:

Note
====

This project has been set up using PyScaffold 4.3.1. For details and usage
information on PyScaffold see https://pyscaffold.org/.
