# Server imports
from flask import Flask, render_template, request, redirect, jsonify
import requests
import json
import pickle
# from ee_config import EE_CREDENTIALS

import time

# Earth Engine import and initialization
import ee

from formatting_date_from_user.get_date_range import get_num_of_days

ee.Initialize()
# ee.Initialize(EE_CREDENTIALS)
# Trigger the authentication flow.
# ee.Authenticate()

app = Flask(__name__)

def county_state_geo_json(state_name, county_name):
    """Determines if county or state geo json needs to be returned"""
    state_name = request.json.get('stateName')
    county_name = request.json.get('countyName')

    state_geo_json = None
    county_geo_json = None


    # Loading GeoJSON shape file
    # Request was made for whole STATE data
    if county_name is None or county_name is "Whole_state":
        print(f'STATE NAME: {state_name}')
        state_file_path = f'coords/states/{state_name}'
        # Read cached GeoJSON
        with open(state_file_path, 'rb') as pickle_file:
            # print(pickle.load(pickle_file))
            # Obtain geo coordinates
            coord_data = pickle.load(pickle_file)[state_name]['coordinates']
            return ee.Geometry.MultiPolygon(coord_data)
            # print(geo_json)

    # Request was made for COUNTY data
    else:
        county_file_path = f'coords/counties/{state_name}/{county_name}'

        # Read cached GeoJSON
        with open(county_file_path, 'rb') as pickle_file:
            # Obtain geo coordinates
            coord_data = pickle.load(pickle_file)[f'{county_name}']['coordinates']

            return ee.Geometry.MultiPolygon(coord_data)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/get_bands')
def get_polygon_data(band_name='LANDSAT/LC08/C01/T1/LC08_044034_20140318'):
    """
        Given Image name, return the available bands to choose from
        Returns: [LIST of STRINGS]
        Args:
            band_name: (str)
     """

    # NOTE: Method from Sam, to extract data from polygon. Refactored from
    # EE Code Editor to Python. Currently not working.

    scale_value = 1000;
    # bands = "tmmn"
    nameOfArea = "polygon"

    # Load the SRTM image.
    collection = ee.ImageCollection("IDAHO_EPSCOR/GRIDMET")

    # TEST IMAGE
    srtm = ee.Image(collection.first()).clip(polygon)
    # //var srtm = ee.Image('CGIAR/SRTM90_V4');

    # Polygon region
    region = ee.Geometry.Rectangle(-122.2806, 37.1209, -122.0554, 37.2413)


    meanDict = srtm.reduceRegion(reducer=ee.Reducer.toList(), geometry=region, scale=30)


    return str(list(meanDict.getInfo().keys()))


    # # Available band names as a list
    # band_names = image.bandNames();

    # return str(band_names)

@app.route('/get_date_data', methods=['GET','POST'])
def get_data_from_date_image():

    image_name = request.json.get('imageName')
    state_name = request.json.get('stateName')
    county_name = request.json.get('countyName')
    start_date = request.json.get('startDate')
    end_date = request.json.get('endDate')
    scale_value = int(request.json.get('scaleValue'))

    print(scale_value)

    delta_days = get_num_of_days(start_date, end_date)

    print(delta_days, start_date, end_date)

    #region = ee.Geometry.Rectangle(-122.2806, 37.1209, -122.0554, 37.2413)
    region = county_state_geo_json(state_name, county_name)

    image_data = ee.ImageCollection(image_name).filterBounds(region).filterDate(start_date,end_date)
    listOfImages = image_data.toList(image_data.size());

    time_start = time.time()


    # NOTE: look into http://www.gevent.org/ to implement paraell processing
    def _mapping_over_date_data(day):

        image = ee.Image(listOfImages.get(day)).clip(region)

        meanDict = image.reduceRegion(reducer= ee.Reducer.mean(), geometry=region, scale=scale_value)


        return meanDict.getInfo()

    all_dicts = map(_mapping_over_date_data, range(delta_days))

    # print(test_all_dicts)

    # OLD CODE: all_dicts created with for loop
    # all_dicts = []

    # for i in range(delta_days):
    #     # print("TEST", i)
    #     image = ee.Image(listOfImages.get(i)).clip(region)
    #     # print("TEST 2", i)
    #     meanDict = image.reduceRegion( reducer= ee.Reducer.mean(), geometry= region, scale= scale_value)
    #
    #     all_dicts.append(meanDict.getInfo())
    #

    print('/get_date_data: \n\n')
    list_all_dicts = list(all_dicts)
    print('Time:', time.time()-time_start)
    print(list_all_dicts)
    print(len(list_all_dicts))


    time_end = time.time()

    print("Total Time:", time_start-time_end)
    # Total Time: -214.62043595314026

    # return str(json.dumps(all_dicts))
    # return str(json.dumps(list(all_dicts)))
    return str(json.dumps(list_all_dicts))





@app.route('/get_data', methods=['GET','POST'])
def get_data_from_image():

    #ee.Initialize()
    # static values

    #nameOfArea = "polygon"
    #region = ee.Geometry.Rectangle(-122.2806, 37.1209, -122.0554, 37.2413)

    # Extract image or image collection name from request
    image_name = request.json.get('imageName')
    state_name = request.json.get('stateName')
    county_name = request.json.get('countyName')
    scale_value = int(request.json.get('scaleValue'))

    # Choosing state_geo_json or county_geo_json based on what is available/requested
    region = county_state_geo_json(state_name, county_name)

    print("TEST **********************")
    print(image_name, state_name, county_name)

    srtm = None
    # Load the SRTM image. Handling error for image vs image collection
    print(srtm)
    image_data = ee.ImageCollection(image_name).filterBounds(region)
    # load image
    srtm = ee.Image(image_data.first()).clip(region)
    try:
        print(srtm.getInfo())
    except:
        print("EXCEPTION_____________")
        # load first image from collection
        srtm = ee.Image(image_name).clip(region)
    #collection = ee.ImageCollection(image_name).filterBounds(region)

    # TEST IMAGE
    #srtm = ee.Image(collection.first()).clip(region)

    # Compute the mean elevation in the polygon.
    meanDict = srtm.reduceRegion( reducer= ee.Reducer.toList(), geometry= region, scale= scale_value)
    # Get the mean from the dictionary and print it.
    # print(meanDict.getInfo())


    # # TEST IMAGE
    first = srtm.clip(region);

    # get image projection
    proj = first.select([0]).projection();

    # get coordinates image
    latlon = ee.Image.pixelLonLat().reproject(proj)
    # Map.addLayer(first, {bands:[bands], min:0, max:500}, 'Image')


    coords = latlon.select(['longitude', 'latitude']).reduceRegion(reducer=ee.Reducer.toList(),
    geometry=region,
    scale=scale_value)


    # get lat & lon
    lat = ee.List(coords.get('latitude'))
    lon = ee.List(coords.get('longitude'))

    #print(lat.getInfo() )
    # zip them. Example: zip([1, 3],[2, 4]) --> [[1, 2], [3,4]]
    #point_list = lon.zip(lat)
    #print('point list', (point_list.getInfo()))
    #print(point_list)
    #csv_data = []


    # TODO: format data to return JSON
    formatted_data = zip_data(lat.getInfo(), lon.getInfo(), meanDict.getInfo())
    # print("test formatted_data")
    # print(formatted_data)

    print("/get_data:")
    print(json.dumps(all_dicts))

    return str(json.dumps(formatted_data))

def zip_data(lat, lon, map_data):
    num = len(lat)

    to_return = {}

    to_return["lat"] = lat[0:num]
    to_return["lon"] = lon[0:num]
    print(to_return)
    for key in map_data:
        to_return[key] = map_data[key]

    return to_return





# # NOTE: sort_feature has to be deafulted to None, but idk what happens if sorted on empty string
# # NOTE: Unsure of what a "scene" is
# # NOTE: Refactored based on Reducing section from https://developers.google.com/earth-engine/getstarted
def get_median_composite(path_to_collection, start_date, end_date, coord_point, num_of_scenes, sort_feature=''):
    """
        Reduce Image Collection to create a median composite over a # of images
        over a date range
        Args:
        path_to_collection (str): Path to image collection
        start_date (str): Start date for date range for image collection in the format
            '<YEAR>-<MONTH>-<DAY>'
        end_date (str): End date for date range for image collection
            '<YEAR>-<MONTH>-<DAY>'
        coord_point (tup): Coordinate geometry point for data extraction (<LATITUDE>, <LONGITUDE>)
        sort_feature (str): Sort data based on dataset feature
        num_of_scenes: (int): Number of scences to limit reduction to
    """

    # Load a Landsat 8 collection.
    collection = ee.ImageCollection(path_to_collection)
    # Filter by date and location.
    collection = collection.filterBounds(ee.Geometry.Point(coord_point[0], coord_point[1])).filterDate(start_date, end_date)
    # Sort by increasing cloudiness.
    collection = collection.sort(sort_feature)

    # Compute the median of each pixel for each band of the 5 least cloudy scenes.
    median = collection.limit(num_of_scenes).reduce(ee.Reducer.median());

    return median

# print(get_median_composite('LANDSAT/LC08/C01/T1', '2014-01-01', '2014-12-31', (-122.262, 37.8719), 5, sort_feature='CLOUD_COVER'))


if __name__ == "__main__":
    app.run(debug=True, port=3000)
