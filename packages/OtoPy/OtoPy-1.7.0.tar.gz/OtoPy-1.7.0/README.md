[![PyPI](https://img.shields.io/pypi/v/OtoPy?label=Package&logo=PyPi)](https://pypi.org/project/OtoPy/)
[![PyPI - Status](https://img.shields.io/pypi/status/OtoPy?logo=pypi)](https://pypi.org/project/OtoPy/)
[![PyPI - Format](https://img.shields.io/pypi/format/OtoPy?logo=pypi)](https://pypi.org/project/OtoPy/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/OtoPy?logo=pypi)](https://pypi.org/project/OtoPy/)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/Otoma-Systems/OtoPy?color=6020A5&label=Release&logo=github)](https://github.com/Otoma-Systems/OtoPy/releases)
[![Build and Deploy on Release](https://github.com/Otoma-Systems/OtoPy/actions/workflows/BuildAndDeploy_OnRelease.yml/badge.svg)](https://github.com/Otoma-Systems/OtoPy/actions/workflows/BuildAndDeploy_OnRelease.yml)
# OtoPy

## Contents
* [Installation](#installation)
* [Importing](#importing)
___

## Installation
  #### New Instalation:
```
pip install OtoPy.
```
  #### Update Package:
```
pip install --upgrade OtoPy.
```
___

## Importing  
  ### Importing specific file from package:
  ```python
  from Otopy import UsefulTools 
  ```
  in this exemple, the ***UsefulTools*** file was entirely imported. For this method of importing the class/function has to be used with the name of the file plus a "." as prefix, like: ***UsefulTools.OLogger***
  
  ### Importing specific function/class from package:
  ```python
  from Otopy.UsefulTools import OLogger
  ```
  in this exemple, only the ***OLogger*** class from ***UsefulTools*** file was imported. For importing multiples classes/functions separate names with comma. For importing all classes/functions from the selected file use "*"
___

![GitHub followers](https://img.shields.io/github/followers/Otoma-Systems?style=social)
