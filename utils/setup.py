import configparser

# Get configuration file
config = configparser.ConfigParser()
config.sections()
config.read('./config/api.ini')
client_id = config.get('main', 'client_id')
client_secret = config.get('main', 'client_secret')
endpoint = config.get('main', 'endpoint')

# Connect to Api
access_url = endpoint+ '?key_identity=' + client_id + '&key_credential=' + client_secret
print("Connected to:    ", access_url)