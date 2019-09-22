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

import pyreadr

result = pyreadr.read_r('gadm36_USA_0_sp.rds') # also works for Rds

# done! let's see what we got
# result is a dictionary where keys are the name of objects and the values python
# objects
print(result.keys()) # let's check what objects we got
df1 = result["df1"] # extract the pandas data frame for object df1

# print(df1)
