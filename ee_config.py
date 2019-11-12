import ee
import os

# Service Account
EE_ACCOUNT = os.environ['GEE_SERVICE_ACCOUNT']

# The private key associated with service account in JSON format.
EE_PRIVATE_KEY_FILE = os.environ['GOOGLE_APPLICATION_CREDENTIALS']

# Authorize connection to EE
EE_CREDENTIALS = ee.ServiceAccountCredentials(EE_ACCOUNT, EE_PRIVATE_KEY_FILE)
