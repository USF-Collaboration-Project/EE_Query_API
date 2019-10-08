import json
import pickle
import os



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
# - Parse State/County GAMD level 2 500k into JSON, CSV, or GoeJSON (DONE)
# - Pickle objects and store in a folder hierarchy: (coords --> states ---> county) (DONE)
# - Process form submission to make GEE query based on unpickled coordinates (Need to do on server)


def parse_state_geojson():
    """
        Script to parse GeoJSON county shapefile and cached the file to server directory

        Args: None
        Return: None
    """

    # Read geojson to string
    with open('gadm36_USA_1.json', 'r') as file:
        data = file.read()

    # parse string to json
    obj = json.loads(data)

    # Static json path to features
    state_data = obj["features"]

    # Parse JSON to seperate state data into seperate files
    for state in state_data:
        # Extract state name
        state_name = state["properties"]["NAME_1"]
        # Extract state geometry
        state_coords = state["geometry"]

        # Write binary file for specific state and cache the file for loading on server
        with open(f'coords/states/{state_name}', 'wb') as geo_file:
            state_obj = {state_name:state_coords}
            pickle.dump(state_obj, geo_file)


def parse_county_geojson():
    """
        Script to parse GeoJSON county shapefile and cached the file to server directory

        Args: None
        Return: None
    """

    # Read geojson to string
    with open('gadm36_USA_2.json', 'r') as file:
        data = file.read()

    # parse string to json
    obj = json.loads(data)

    # Static json path to features
    county_data = obj["features"]

    # Parse county json to seperate cached files
    for county in county_data:
        # Extract State and County name
        state_name = county["properties"]["NAME_1"]
        county_name = county["properties"]["NAME_2"]
        # Extact county geomety
        county_coords = county["geometry"]

        # Static formated file paths
        state_file_path = f'coords/counties/{state_name}'
        county_file_path = f'coords/counties/{state_name}/{county_name}'

        # If state directory doesn't exist, create it
        # Seperating county data into state folders in case there are counties in different
        # states with the same name
        if not os.path.exists(state_file_path):
            os.makedirs(state_file_path)

        # Write binary file for specific county and cache the file
        with open(county_file_path, 'wb') as geo_file:
            county_obj = {county_name:county_coords}
            pickle.dump(county_obj, geo_file)


if __name__ == "__main__":

    # NOTE: Uncomment to parse state/county GeoJSON shape files
    # parse_state_geojson()
    # parse_county_geojson()

    # NOTE: MOVE TO MAIN SERVER FILE
    # Read cached GeoJSON
    # with open(f'coords/states/{state_name}', 'rb') as pickle_file:
    #     geo_json = pickle.load(pickle_file)
    #     print(geo_json)
