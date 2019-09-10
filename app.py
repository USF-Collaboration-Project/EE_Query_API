# Import the Earth Engine library.
import ee

# Trigger the authentication flow.
# ee.Authenticate()

ee.Initialize()


def print_elevation_ME():
    """ Print the elevation of Mount Everest."""
    dem = ee.Image('USGS/SRTMGL1_003')
    xy = ee.Geometry.Point([86.9250, 27.9881])
    elev = dem.sample(xy, 30).first().get('elevation').getInfo()
    print('Mount Everest elevation (m):', elev)
    return


def print_obj_info():
    """ Printing EE object info """
    # Load a Landsat image
    img = ee.Image('LANDSAT/LT05/C01/T1_SR/LT05_034033_20000913')

    # Print image object WITHOUT call to getInfo(); prints serialized request instructions
    # print(img)

    # Print image object WITH call to getInfo(); prints image metadata
    print(img.getInfo())

    return



def exporting_data():
    task = ee.batch.Export.image.toDrive(image=myImg,
                                     region=myRegion.getInfo()['coordinates'],
                                     description='myDescription',
                                     folder='myGDriveFolder',
                                     fileNamePrefix='myFilePrefix',
                                     scale=myScale,
                                     crs=myCRS)

    task.start()
    task.status()
    return




# print_elevation_ME()
print_obj_info()
