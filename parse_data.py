# gadm36_USA_0_sp.rds

"""
    Geospatial data is being obtained from https://gadm.org/index.html
    We are utilizing the Shapefile for the United States, extracting geospatial Geometry
    coordinates at different two levels: state and county. Below describes what the levels
    mean in the context of the files inside the Shapefile

    Level 0: Country as a whole (Useful when we scale to global coordinates)
    Level 1: State
    Level 2: Counties

    Extract Coordinate Geometry From Shapefile:

    Use https://mapshaper.org/ to import the shapefile for the level of data desired
    and then import the corresponding .prj, .dbf, and .shx files to the mapshaper. Finally
    export the data as GeoJSON.

"""

# TODO:
# - Parse State/County GAMD level 2 500k into JSON, CSV, or GoeJSON
# - Pickle objects and store in a folder hierarchy: (coords --> states ---> county)
# - Process form submission to make GEE query based on unpickled coordinates 

import json

with open('gadm36_USA_1.json', 'r') as file:
    data = file.read()

# parse string to json
obj = json.loads(data)

# Prints name of State
print(obj["features"][0]["properties"]["NAME_1"])


# {'GID_0': 'USA', 'NAME_0': 'United States', 'GID_1': 'USA.1_1', 'NAME_1': 'Alabama', 'VARNAME_1':
# 'AL|Ala.', 'NL_NAME_1': '', 'TYPE_1': 'State', 'ENGTYPE_1': 'State', 'CC_1': '', 'HASC_1': 'US.AL'
# }
