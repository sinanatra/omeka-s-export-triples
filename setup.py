import configparser

config = configparser.ConfigParser()
config.sections()
config.read('./config/api.ini')

client_id = config.get('main', 'client_id')
client_secret = config.get('main', 'client_secret')
endpoint = config.get('main', 'endpoint')

print(client_secret)