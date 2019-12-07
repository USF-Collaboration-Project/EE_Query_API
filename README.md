# Google Earth Engine Querying API for Dataset Generation

Mircoservice Query API for {INSERT NAME OF MAIN APP}. This API queries the Google Earth Engine API based on the custom queries specified by our users (geospatial researchers).

API called from: {INSERT GITHUB PAGE LINK TO FORM SUBMISSION}

# API Endpoints

### /get_data, methods=['GET','POST']

Send fetch call to 'https://ee-query-api.herokuapp.com/get_data' sending along an options object in the following format:

    const options = {
      method: 'post',
      body: JSON.stringify({
        imageName: value,
        stateName: stateChoice,
        countyName: countyChoice,
      }),
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      }
    }

Returns ---> JSON:
__NOTE: Number of keys = days in specified date range (date range starts from 0)__

    Key: Day number <INTEGER>
    Value: Dictionary of results for each band for the day

    Example:

    {
        0: {<band_name>: <band_value>, <band_name>: <band_value>, <band_name>: <band_value>, <band_name>: <band_value>, <band_name>:<band_value>, …}
        1: {<band_name>: <band_value>, <band_name>: <band_value>, <band_name>: <band_value>, <band_name>: <band_value>, <band_name>: <band_value>, …},
        ...
    }



# Installation and How To Use

    <Add requirements.txt>
    <Versions of Earth Engine API:>
    https://pypi.org/project/earthengine-api/0.1.201/



# Optimizations
Multiprocessing through Earth Engine IDE:
https://developers.google.com/earth-engine/tutorial_js_03


# Next Steps


# Frameworks used and external resources:
* Flask
* JS
* Highcharts visualizations
* Geospatial shape files: https://gadm.org/
