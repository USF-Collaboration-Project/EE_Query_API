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
        <ADD JSON example>




# Installation and How To Use
