# JupyterHub Notebook Container Setup
This repository contains the software responsible for setting up Jupyter Hub Container for a FABRIC user.

## Overview



## Requirements
Python 3.9+

## Pre-requisites
Ensure that following are installed
```
virtualenv
virtualenvwrapper
```
## Installation
Multiple installation options possible. For CF development the recommended method is to install from GitHub MASTER branch:
```
$ mkvirtualenv fabrictestbed
$ workon fabrictestbed
$ pip install git+https://github.com/fabric-testbed/fabric-cli.git
```
For inclusion in tools, etc, use PyPi
```
$ mkvirtualenv fabrictestbed
$ workon fabrictestbed
$ pip install fabrictestbed
```