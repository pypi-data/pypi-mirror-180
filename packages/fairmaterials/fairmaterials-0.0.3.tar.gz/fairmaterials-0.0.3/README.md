
![logo](https://i.imgur.com/pqR2OBe.png)

# Fairmaterials
Fairmaterials is a tool for fairing data. It reads a template JSON file to get the preset data. The user can edit the data by manually inputting or by importing a csv file. The final output will be a new JSON file with the same structure. 


# Features
 -  Importing JSON template as JSON-LD.
 -   Display fair data in dataframe format.
 -   Automatically notify duplicate names.
 -   Modify JSON data.
		- Based on CSV file.
		- Based on keyboard input.
 -   Output as standard JSON-LD.
 
#  Setup
1. Install it at bash
```bash
$ pip install fairmaterials
```
2.	Import it in python
```python
from fairmaterials.fairy_csv import *
``` 
#  A quick example
***Select a domain***
```python
fairy_data("OpticalSpc")
``` 
***Output will be json-ld format file***

#  Versions
All notable changes to this project will be documented in this file.
## [0.0.3] - 2022-12-10
### Added
- Add fairy_data function
## [0.0.213] - 2022-10-8
### Added
- Add template csv file.
## [0.0.212] - 2021-10-7
### Added
- Add group input CSV file generation function.
- Add directly convert a group input CSV file to multiple json file function.
- Add Version part in Readme.md file.