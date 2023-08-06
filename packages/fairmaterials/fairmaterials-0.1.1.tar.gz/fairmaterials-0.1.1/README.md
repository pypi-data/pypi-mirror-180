
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
from fairmaterials.fairify import *
``` 
#  A quick example
***Select a domain***
```python
fairify_data("XRD")
``` 
***Output will be series of json-ld format file***

#  Versions
All notable changes to this project will be documented in this file.
## [0.1.0] - 2022-12-10
### Added
- Add fairy_data function,user can select domains to fairy data
#### Domains
- XRD
- CapillaryElectrophoresis
- PolymerAM
- PVModule
- PolymerBacksheets
- OpticalSpectroscopy
- Buildings
- GeospatialWell
- MetalAM
- OpticalProfilometry
- PVSystem
- XCT 

## [0.0.213] - 2022-10-8
### Added
- Add template csv file.
## [0.0.212] - 2021-10-7
### Added
- Add group input CSV file generation function.
- Add directly convert a group input CSV file to multiple json file function.
- Add Version part in Readme.md file.

## Funding Acknowledgements:
This work was supported by the U.S. Department of Energy’s Office of Energy Efficiency and Renewable Energy (EERE) under Solar Energy Technologies Office (SETO) Agreement Numbers DE-EE0009353 and DE-EE0009347, Department of Energy (National Nuclear Security Administration) under Award Number DE-NA0004104 and Contract number B647887, and U.S. National Science Foundation Award under Award Number 2133576.