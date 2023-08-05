.. image:: ./docs/images/favicon/limax-100x100-300dpi.png
   :align: left
   :alt: limax logo

limax: python utilities for LiMAx
==============================================================

.. image:: https://github.com/matthiaskoenig/limax/workflows/CI-CD/badge.svg
   :target: https://github.com/matthiaskoenig/limax/workflows/CI-CD
   :alt: GitHub Actions CI/CD Status

.. image:: https://img.shields.io/pypi/v/limax.svg
   :target: https://pypi.org/project/limax/
   :alt: Current PyPI Version

.. image:: https://img.shields.io/pypi/pyversions/limax.svg
   :target: https://pypi.org/project/limax/
   :alt: Supported Python Versions

.. image:: https://img.shields.io/pypi/l/limax.svg
   :target: http://opensource.org/licenses/LGPL-3.0
   :alt: GNU Lesser General Public License 3

.. image:: https://codecov.io/gh/matthiaskoenig/limax/branch/develop/graph/badge.svg
   :target: https://codecov.io/gh/matthiaskoenig/limax
   :alt: Codecov

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.5308801.svg
   :target: https://doi.org/10.5281/zenodo.5308801
   :alt: Zenodo DOI

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/ambv/black
   :alt: Black

.. image:: http://www.mypy-lang.org/static/mypy_badge.svg
   :target: http://mypy-lang.org/
   :alt: mypy

limax is a collection of python utilities for working with
LiMAx data with source code available from 
`https://github.com/matthiaskoenig/limax <https://github.com/matthiaskoenig/limax>`__.

Features include among others

- Visualization of LiMAx raw data
- Anonymisation of LiMAx raw data files
- Calculation of AUC and DOB values
 
If you have any questions or issues please `open an issue <https://github.com/matthiaskoenig/limax/issues>`__.

Documentation
=============
Documentation is still work in progress.

How to cite
===========

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.5308801.svg
   :target: https://doi.org/10.5281/zenodo.5308801
   :alt: Zenodo DOI

Installation
============
`limax` is available from `pypi <https://pypi.python.org/pypi/limax>`__ and 
can be installed via:: 

    pip install limax

Best practise is to setup a virtual environment example via conda and install the package.
First install anaconda via https://docs.anaconda.com/anaconda/install/index.html::

    conda create -n limax python=3.10
    conda activate limax
    (limax) pip install limax --upgrade



Usage
=====

Command line tool
-----------------

After installation LiMAx analysis can be performed using the :code:`limax` command line tool

.. code:: bash

    $ limax
    
    ────────────────────────────────────────────────────────────────────────────────
    💉 LIMAX ANALYSIS 💉
    Version 0.1.0 (https://github.com/matthiaskoenig/limax)
    Citation https://doi.org/10.5281/zenodo.3708271
    ────────────────────────────────────────────────────────────────────────────────
    Required argument '--input' missing
    Usage: limax [options]
    
    Options:
      -h, --help            show this help message and exit
      -i INPUT_PATH, --input=INPUT_PATH
                            Path to LiMAx raw file.
      -o OUTPUT_PATH, --output=OUTPUT_PATH
                            Path to processed LiMAx file (without patient data) as
                            '*.csv'.
    ────────────────────────────────────────────────────────────────────────────────

License
=======
* Source Code: `LGPLv3 <http://opensource.org/licenses/LGPL-3.0>`__
* Documentation: `CC BY-SA 4.0 <http://creativecommons.org/licenses/by-sa/4.0/>`__

The limax source is released under both the GPL and LGPL licenses version 2 or
later. You may choose which license you choose to use the software under.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License or the GNU Lesser General Public
License as published by the Free Software Foundation, either version 2 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU General Public License for more details.

Funding
=======
Matthias König is supported by the Federal Ministry of Education and Research (BMBF, Germany)
within the research network Systems Medicine of the Liver (**LiSyM**, grant number 031L0054) 
and by the German Research Foundation (DFG) within the Research Unit Programme FOR 5151 
"`QuaLiPerF <https://qualiperf.de>`__ (Quantifying Liver Perfusion-Function Relationship in Complex Resection - 
A Systems Medicine Approach)" by grant number 436883643 and by grant number 465194077 (Priority Programme SPP 2311, Subproject SimLivA).

Develop version
===============
The latest develop version can be installed via::

    pip install git+https://github.com/matthiaskoenig/limax.git@develop

Or via cloning the repository and installing via::

    git clone https://github.com/matthiaskoenig/limax.git
    cd limax
    pip install -e .

To install for development use::

    pip install -e .[development]


© 2022 Matthias König
