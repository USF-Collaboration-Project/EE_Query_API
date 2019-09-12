# Server imports
from flask import Flask, render_template, request, redirect
import requests
# Earth Engine import and initialization
import ee
# Trigger the authentication flow.
# ee.Authenticate()
ee.Initialize()


app = Flask(__name__)


@app.route('/')

# NOTE: sort_feature has to be deafulted to None, but idk what happens if sorted on empty string
# NOTE: Unsure of what a "scene" is
# NOTE: Refactored based on Reducing section from https://developers.google.com/earth-engine/getstarted
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

print(get_median_composite('LANDSAT/LC08/C01/T1', '2014-01-01', '2014-12-31', (-122.262, 37.8719), 5, sort_feature='CLOUD_COVER'))


if __name__ == "__main__":
    app.run(degbug=True, port=5000)
