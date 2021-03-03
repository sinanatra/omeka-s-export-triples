from rdflib import Graph, plugin
from rdflib.serializer import Serializer
from utils.setup import *
import urllib.request

resource_id = 15
resource_url = endpoint + str("/" + str(resource_id))
page = urllib.request.urlopen(resource_url)
resource_content = page.read().decode('utf-8')
g = Graph().parse(data=resource_content, format='json-ld')
print(g.serialize(format='xml', indent=4).decode('utf-8'))