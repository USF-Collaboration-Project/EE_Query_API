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
*NOTE: Number of keys = days in specified date range (date range starts from 0)*

    Key: Day number <INTEGER>
    Value: Dictionary of results for each band for the day <HASHMAP>

    Example:

    {
        0: {<BAND_NAME>: <band_value>, <BAND_NAME>: <band_value>, <BAND_NAME>: <band_value>, <BAND_NAME>: <band_value>, <BAND_NAME>:<band_value>, …}
        1: {<BAND_NAME>: <band_value>, <BAND_NAME>: <band_value>, <BAND_NAME>: <band_value>, <BAND_NAME>: <band_value>, <BAND_NAME>: <band_value>, …},
        ...
    }


# Installation and How To Use

### Local:
* git clone https://github.com/USF-Collaboration-Project/EE_Query_API.git
* cd EE_Query_API
* pip install -r requirements.txt *Certain versions of the Google Earth Engine API throws errors like "unfound String.IO module". We found that version 0.1.201(https://pypi.org/project/earthengine-api/0.1.201/) works well in deployment which is what we've also specified in the requirements.txt*

* Visit https://signup.earthengine.google.com/#!/ and sign up to use Google Earth Engine. Now wait until you've received a confirmation email (it may take a day or two).

* Make sure that the lines containing `ee.Initialize()` and `ee.Authenticate()` are uncommented and then run: python app.py *After you authenticate once, you may comment out ee.Authenticate*

* Fill out the form for desired dataset, dataset image, state or county from which you want data from, date range, scale value, etc. Once you've submitted the request, it may take some moments to retrieve the data from the API, it all depends on how big of a geospatial region you selected to extract data from as well as how 'detailed' the query is (scale value).

* Once a mock CSV appears on screen, the user may click on the different bands to visualize a time series graph of that band across the specified date range. This is meant to get a sense of what story the data is trying to show us.

* If the dataset is to the user's specifications, then they may click the "download csv" button to the desired destination path.

### Deployment:

__For usage:__
* Almost same as above, only skip all the registering and project configuration. Just visit https://ee-query-api.herokuapp.com/ and follow the last three points the Local Installation portion above.

__For Contributors:__
* In deployment the application requires requests to be made to the Google Earth Engine API via a service account, not the registered account you made for local usage https://developers.google.com/earth-engine/service_account.

* Save private information from registered service account into environment variables or configuration variables in whatever deployment service being used (currently Heroku).

* Create a new file to create ee.ServiceAccountCredentials object *see ee_config.py for how to set it up*

* When you push to deployment make sure `ee.Initialize(EE_CREDENTIALS)` is uncommented and `ee.Initialize()` is commented out. Swap out the EE_CREDENTIALS argument with the ee.ServiceAccountCredentials object you created before.


## Optimizations
Multiprocessing requests through Earth Engine IDE:
https://developers.google.com/earth-engine/tutorial_js_03


## Next Steps
* Large query compatibity (avoid timeouts)
* More geospatial files for different regions
* Allow custom geospatial objects to be sent along a request

## Frameworks used and external resources:
* Flask
* JS
* Highcharts visualizations
* Geospatial shape files: https://gadm.org/
