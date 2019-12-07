# Google Earth Engine Querying API for Dataset Generation
We are providing an easy to use API generate custom geospatial datasets by extracting the GEE API  

# Users
* Geospatial researchers

# API Endpoints

### '/get_data', methods=['GET','POST']


    Send POST request to 'https://git.heroku.com/ee-query-api.git/get_data' sending along  an options object in the following format (See Index html this repo for example fetch request)

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

    Returns (JSON):
        *NOTE: Number of keys = days in specified date range (date range starts from 0)*

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
