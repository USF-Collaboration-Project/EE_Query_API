
"""
Python Playground for testing EE

Python implementation examples:
https://github.com/google/earthengine-api/tree/master/python/examples/py/Image

"""

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
    """ Exporting Region data to the cloud"""
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


def get_image_metadata(image):
    # NOTE: just data ABOUT the image, not the image data
    """ Image information and metadata """

    # Get information about the bands as a list.
    bandNames = image.bandNames();
    print('Band names:', bandNames); # ee.List of band names



def test_get_image_metadata():
    image = ee.Image('LANDSAT/LC08/C01/T1/LC08_044034_20140318');
    metadata = get_image_metadata()
    print(metadata)



polygon = ee.Geometry.MultiPolygon(
  [ [ [ [ -71.281571, 41.648207 ], [ -71.278171, 41.647309 ], [ -71.274315, 41.638125 ], [ -71.283791, 41.637797 ], [ -71.286755, 41.642725 ], [ -71.283005, 41.644434 ], [ -71.281571, 41.648207 ] ] ], [ [ [ -71.331200, 41.580318 ], [ -71.335949, 41.585898 ], [ -71.337048, 41.594688 ], [ -71.333751, 41.605859 ], [ -71.329559, 41.609097 ], [ -71.326609, 41.616114 ], [ -71.325877, 41.623988 ], [ -71.333305, 41.629536 ], [ -71.346570, 41.632229 ], [ -71.362869, 41.651457 ], [ -71.366165, 41.660980 ], [ -71.348402, 41.663727 ], [ -71.338696, 41.658782 ], [ -71.336182, 41.647961 ], [ -71.337048, 41.646146 ], [ -71.342514, 41.644791 ], [ -71.343666, 41.639900 ], [ -71.330711, 41.632992 ], [ -71.314889, 41.630398 ], [ -71.305550, 41.622523 ], [ -71.303352, 41.606591 ], [ -71.307381, 41.597984 ], [ -71.317474, 41.583187 ], [ -71.326103, 41.578583 ], [ -71.331200, 41.580318 ] ] ], [ [ [ -71.120570, 41.497448 ], [ -71.136867, 41.493942 ], [ -71.141093, 41.489937 ], [ -71.140224, 41.485855 ], [ -71.167345, 41.471405 ], [ -71.170131, 41.463974 ], [ -71.193020, 41.457931 ], [ -71.194967, 41.459037 ], [ -71.196857, 41.461116 ], [ -71.196607, 41.464756 ], [ -71.190016, 41.478275 ], [ -71.190167, 41.484285 ], [ -71.199390, 41.491769 ], [ -71.199692, 41.495511 ], [ -71.206382, 41.499215 ], [ -71.200788, 41.514371 ], [ -71.213563, 41.545818 ], [ -71.208650, 41.571028 ], [ -71.207780, 41.600660 ], [ -71.212656, 41.610072 ], [ -71.212417, 41.618290 ], [ -71.212004, 41.622990 ], [ -71.216160, 41.625490 ], [ -71.240709, 41.619225 ], [ -71.243600, 41.587508 ], [ -71.236130, 41.574767 ], [ -71.236642, 41.535852 ], [ -71.234775, 41.532538 ], [ -71.227989, 41.528297 ], [ -71.229444, 41.521544 ], [ -71.240614, 41.500557 ], [ -71.246047, 41.492983 ], [ -71.247422, 41.490234 ], [ -71.243641, 41.486453 ], [ -71.237175, 41.486546 ], [ -71.236751, 41.483369 ], [ -71.240710, 41.474872 ], [ -71.246703, 41.471960 ], [ -71.245992, 41.481302 ], [ -71.252692, 41.485902 ], [ -71.264793, 41.488902 ], [ -71.275324, 41.479594 ], [ -71.282260, 41.487983 ], [ -71.285639, 41.487805 ], [ -71.295111, 41.484350 ], [ -71.296516, 41.479831 ], [ -71.295885, 41.468580 ], [ -71.300438, 41.467220 ], [ -71.304394, 41.454502 ], [ -71.311394, 41.450802 ], [ -71.312694, 41.451402 ], [ -71.312718, 41.454597 ], [ -71.321410, 41.455600 ], [ -71.337695, 41.448902 ], [ -71.351096, 41.450802 ], [ -71.356033, 41.449332 ], [ -71.358656, 41.457019 ], [ -71.362743, 41.460379 ], [ -71.361520, 41.464831 ], [ -71.347819, 41.470898 ], [ -71.336442, 41.481985 ], [ -71.334380, 41.478204 ], [ -71.335992, 41.469647 ], [ -71.316519, 41.477560 ], [ -71.317414, 41.488776 ], [ -71.323125, 41.503088 ], [ -71.327804, 41.504258 ], [ -71.330694, 41.507699 ], [ -71.330831, 41.518364 ], [ -71.313079, 41.534672 ], [ -71.310533, 41.546920 ], [ -71.303652, 41.559925 ], [ -71.294363, 41.571416 ], [ -71.288376, 41.573274 ], [ -71.285142, 41.577127 ], [ -71.289073, 41.582706 ], [ -71.285635, 41.591642 ], [ -71.278806, 41.593302 ], [ -71.273445, 41.606990 ], [ -71.272412, 41.615041 ], [ -71.275234, 41.619444 ], [ -71.271862, 41.623986 ], [ -71.251082, 41.638780 ], [ -71.233234, 41.640230 ], [ -71.220331, 41.655572 ], [ -71.217513, 41.641508 ], [ -71.212136, 41.641945 ], [ -71.195640, 41.675090 ], [ -71.194390, 41.674802 ], [ -71.191178, 41.674216 ], [ -71.191175, 41.674292 ], [ -71.181290, 41.672502 ], [ -71.175990, 41.671402 ], [ -71.176090, 41.668502 ], [ -71.176090, 41.668102 ], [ -71.153989, 41.664102 ], [ -71.145870, 41.662795 ], [ -71.135188, 41.660502 ], [ -71.134688, 41.660502 ], [ -71.132888, 41.660102 ], [ -71.132670, 41.658744 ], [ -71.134478, 41.641262 ], [ -71.134484, 41.641198 ], [ -71.135688, 41.628402 ], [ -71.140468, 41.623893 ], [ -71.141509, 41.616076 ], [ -71.140910, 41.607405 ], [ -71.140588, 41.605102 ], [ -71.137492, 41.602561 ], [ -71.131618, 41.593918 ], [ -71.131312, 41.592308 ], [ -71.122400, 41.522156 ], [ -71.120570, 41.497448 ] ] ], [ [ [ -71.326769, 41.491286 ], [ -71.325365, 41.487601 ], [ -71.327822, 41.482985 ], [ -71.343013, 41.495615 ], [ -71.341122, 41.498598 ], [ -71.326769, 41.491286 ] ] ], [ [ [ -71.383586, 41.464782 ], [ -71.389284, 41.460605 ], [ -71.390275, 41.455043 ], [ -71.399568, 41.448596 ], [ -71.400560, 41.460940 ], [ -71.395927, 41.492215 ], [ -71.386511, 41.493071 ], [ -71.378914, 41.504948 ], [ -71.391005, 41.514578 ], [ -71.392137, 41.524468 ], [ -71.384478, 41.556736 ], [ -71.379021, 41.567772 ], [ -71.373618, 41.573214 ], [ -71.370194, 41.573963 ], [ -71.363560, 41.570860 ], [ -71.359868, 41.556308 ], [ -71.363292, 41.501952 ], [ -71.360403, 41.483121 ], [ -71.354315, 41.478891 ], [ -71.380947, 41.474561 ], [ -71.383586, 41.464782 ] ] ], [ [ [ -71.224798, 41.710498 ], [ -71.227875, 41.705498 ], [ -71.240991, 41.697744 ], [ -71.237635, 41.681635 ], [ -71.241550, 41.667205 ], [ -71.259560, 41.642595 ], [ -71.267055, 41.644945 ], [ -71.270075, 41.652439 ], [ -71.269180, 41.654900 ], [ -71.280366, 41.672575 ], [ -71.287637, 41.672463 ], [ -71.290546, 41.662395 ], [ -71.299159, 41.649531 ], [ -71.301396, 41.649978 ], [ -71.303746, 41.654788 ], [ -71.306095, 41.672575 ], [ -71.302627, 41.681747 ], [ -71.298935, 41.681524 ], [ -71.293119, 41.688347 ], [ -71.291217, 41.702666 ], [ -71.298800, 41.711008 ], [ -71.301446, 41.706441 ], [ -71.308634, 41.711026 ], [ -71.305759, 41.718662 ], [ -71.314820, 41.723808 ], [ -71.342786, 41.728506 ], [ -71.350057, 41.727835 ], [ -71.353748, 41.724702 ], [ -71.365717, 41.711615 ], [ -71.365717, 41.694947 ], [ -71.372988, 41.672575 ], [ -71.377910, 41.666646 ], [ -71.382049, 41.667317 ], [ -71.389880, 41.671903 ], [ -71.390775, 41.680629 ], [ -71.389432, 41.683425 ], [ -71.390551, 41.684096 ], [ -71.418069, 41.684208 ], [ -71.441336, 41.686446 ], [ -71.443082, 41.688303 ], [ -71.441896, 41.690025 ], [ -71.445923, 41.691144 ], [ -71.449318, 41.687401 ], [ -71.444468, 41.664409 ], [ -71.430038, 41.667541 ], [ -71.425452, 41.670785 ], [ -71.409302, 41.662643 ], [ -71.403770, 41.589321 ], [ -71.447712, 41.580400 ], [ -71.442567, 41.565075 ], [ -71.421649, 41.537892 ], [ -71.417398, 41.534536 ], [ -71.414825, 41.523126 ], [ -71.414937, 41.516303 ], [ -71.421425, 41.498629 ], [ -71.419971, 41.484758 ], [ -71.417957, 41.482073 ], [ -71.417621, 41.477934 ], [ -71.418404, 41.472652 ], [ -71.421157, 41.469888 ], [ -71.422991, 41.472682 ], [ -71.430744, 41.470636 ], [ -71.430926, 41.465655 ], [ -71.427935, 41.459529 ], [ -71.428652, 41.454158 ], [ -71.433612, 41.444995 ], [ -71.437670, 41.441302 ], [ -71.441199, 41.441602 ], [ -71.448948, 41.438479 ], [ -71.455845, 41.432986 ], [ -71.455371, 41.407962 ], [ -71.474918, 41.386104 ], [ -71.483295, 41.371722 ], [ -71.479867, 41.361125 ], [ -71.487772, 41.361125 ], [ -71.502926, 41.373665 ], [ -71.513401, 41.374702 ], [ -71.526724, 41.376636 ], [ -71.555381, 41.373316 ], [ -71.624505, 41.360870 ], [ -71.688070, 41.342823 ], [ -71.701631, 41.336968 ], [ -71.720740, 41.331567 ], [ -71.773702, 41.327977 ], [ -71.785957, 41.325739 ], [ -71.833755, 41.315631 ], [ -71.857432, 41.306318 ], [ -71.862772, 41.309791 ], [ -71.862109, 41.316612 ], [ -71.860513, 41.320248 ], [ -71.839013, 41.334042 ], [ -71.829595, 41.344544 ], [ -71.835951, 41.353935 ], [ -71.837738, 41.363529 ], [ -71.831613, 41.370899 ], [ -71.833443, 41.384524 ], [ -71.842131, 41.395359 ], [ -71.843472, 41.405830 ], [ -71.842563, 41.409855 ], [ -71.839649, 41.412119 ], [ -71.818390, 41.419599 ], [ -71.797683, 41.416709 ], [ -71.789356, 41.596910 ], [ -71.786994, 41.655992 ], [ -71.789678, 41.724734 ], [ -71.791062, 41.770273 ], [ -71.792767, 41.807001 ], [ -71.792786, 41.808670 ], [ -71.794161, 41.840141 ], [ -71.794161, 41.841101 ], [ -71.797922, 41.935395 ], [ -71.799242, 42.008065 ], [ -71.766010, 42.009745 ], [ -71.576908, 42.014098 ], [ -71.559439, 42.014342 ], [ -71.527606, 42.014998 ], [ -71.527306, 42.015098 ], [ -71.500905, 42.017098 ], [ -71.499905, 42.017198 ], [ -71.381401, 42.018798 ], [ -71.381501, 41.966699 ], [ -71.381401, 41.964799 ], [ -71.381600, 41.922899 ], [ -71.381700, 41.922699 ], [ -71.381700, 41.893199 ], [ -71.376600, 41.893999 ], [ -71.373799, 41.894399 ], [ -71.370999, 41.894599 ], [ -71.365399, 41.895299 ], [ -71.364699, 41.895399 ], [ -71.362499, 41.895599 ], [ -71.354699, 41.896499 ], [ -71.352699, 41.896699 ], [ -71.338698, 41.898399 ], [ -71.339298, 41.893599 ], [ -71.339298, 41.893399 ], [ -71.340798, 41.881600 ], [ -71.333997, 41.862300 ], [ -71.342198, 41.844800 ], [ -71.341797, 41.843700 ], [ -71.335197, 41.835500 ], [ -71.337597, 41.833700 ], [ -71.339597, 41.832000 ], [ -71.344897, 41.828000 ], [ -71.347197, 41.823100 ], [ -71.339197, 41.809000 ], [ -71.338897, 41.808300 ], [ -71.339297, 41.806500 ], [ -71.339297, 41.804400 ], [ -71.340797, 41.800200 ], [ -71.340697, 41.798300 ], [ -71.339297, 41.796300 ], [ -71.335797, 41.794800 ], [ -71.333896, 41.794500 ], [ -71.332196, 41.792300 ], [ -71.329296, 41.786800 ], [ -71.329396, 41.782600 ], [ -71.327896, 41.780501 ], [ -71.317795, 41.776101 ], [ -71.261392, 41.752301 ], [ -71.225791, 41.711701 ], [ -71.224798, 41.710498 ] ] ], [ [ [ -71.589550, 41.196557 ], [ -71.580228, 41.204837 ], [ -71.577301, 41.214710 ], [ -71.576661, 41.224434 ], [ -71.573785, 41.228436 ], [ -71.561093, 41.224207 ], [ -71.555006, 41.216822 ], [ -71.554067, 41.212957 ], [ -71.557459, 41.204542 ], [ -71.564119, 41.195372 ], [ -71.565752, 41.184373 ], [ -71.560969, 41.176186 ], [ -71.550226, 41.166787 ], [ -71.544446, 41.164912 ], [ -71.543872, 41.161321 ], [ -71.547051, 41.153684 ], [ -71.551953, 41.151718 ], [ -71.593700, 41.146339 ], [ -71.599993, 41.146932 ], [ -71.611706, 41.153239 ], [ -71.613133, 41.160281 ], [ -71.605565, 41.182139 ], [ -71.594994, 41.188392 ], [ -71.589550, 41.196557 ] ] ] ]);

def get_mean_elevation():
    # Load the SRTM image.
    srtm = ee.Image('CGIAR/SRTM90_V4');

    # Apply an algorithm to an image.
    slope = ee.Terrain.slope(srtm);
    # Display the result.
    # Map.setCenter(-112.8598, 36.2841, 9); # Center on the Grand Canyon.
    # Map.addLayer(slope, {min: 0, max :60}, 'slope');

    # Compute the mean elevation in the polygon.
    meanDict = srtm.reduceRegion({
      reducer: ee.Reducer.toList(),
      geometry: polygon,
      scale: 90
    });

    # Get the mean from the dictionary and print it.
    mean = meanDict.get('elevation');
    print('Mean elevation', mean);



def filter_and_sort():
    """ Filter and sort image collections based on regions and dataset features """
    point = ee.Geometry.Point(-122.262, 37.8719)
    start = ee.Date('2014-06-01');
    finish = ee.Date('2014-10-01');
    filteredCollection = ee.ImageCollection('LANDSAT/LC08/C01/T1').filterBounds(point).filterDate(start, finish).sort('CLOUD_COVER', True)

    return filteredCollection


# def get_polygon_data():
#     # NOTE: Method from Sam, to extract data from polygon. Refactored from
#     # EE Code Editor to Python. Currently not working.
#     """ Extract data from image to csv """
#
#     scale_value = 1000;
#     bands = "tmmn"
#     nameOfArea = "polygon"
#
#     # Load the SRTM image.
#     collection = ee.ImageCollection("IDAHO_EPSCOR/GRIDMET").filterBounds(polygon);
#
#     # TEST IMAGE
#     srtm = ee.Image(collection.first()).clip(polygon)
#     # //var srtm = ee.Image('CGIAR/SRTM90_V4');
#
#     print(srtm)
#
#
#     # Compute the mean elevation in the polygon.
#     meanDict = srtm.reduceRegion({
#     reducer: ee.Reducer.toList(),
#     geometry: polygon,
#     scale: scale_value
#     });
#
#     print('meanDict', meanDict);
#
#     # Get the mean from the dictionary and print it.
#     mean = meanDict.get('elevation');
#     print('Mean elevation', mean);
#
#
#     # TEST IMAGE
#     first = srtm.clip(polygon);
#
#     # get image projection
#     proj = first.select([0]).projection();
#
#     # get coordinates image
#     latlon = ee.Image.pixelLonLat().reproject(proj)
#     # Map.addLayer(first, {bands:[bands], min:0, max:500}, 'Image')
#
#     # put each lon lat in a list
#     coords = latlon.select(['longitude', 'latitude']).reduceRegion({
#         reducer: ee.Reducer.toList(),
#         geometry: polygon,
#         scale: scale_value
#       })
#
#     # get lat & lon
#     lat = ee.List(coords.get('latitude'))
#     lon = ee.List(coords.get('longitude'))
#
#     # zip them. Example: zip([1, 3],[2, 4]) --> [[1, 2], [3,4]]
#     point_list = lon.zip(lat)
#     print('point list', point_list)
#     csv_data = []
#
#     print(point_list.length)
#
#
#     # NOTE: Need to refactor to python
#     computeData = function(point){
#         p = ee.Geometry.Point(point)
#         dataPoint = srtm
#         .select(bands)
#         .reduceRegion(ee.Reducer.first(),p,scale_value)
#         .get(bands)
#
#         return [point,ee.Number(dataPoint)]
#       }
#
#       csv_data = point_list.map(computeData)
#       return csv_data
#       print(csv_data)



print(filter_and_sort())

# get_polygon_data()


# print_elevation_ME()
# print_obj_info()


# test_get_image_metadata()
# get_polygon_data()
