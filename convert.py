from rdflib import Graph, Literal, Namespace, RDF, URIRef, plugin
from rdflib.serializer import Serializer
import argparse
import urllib.request
from utils.setup import *
import json

graph = Graph()
skos = Namespace('http://www.w3.org/2004/02/skos/core#')
graph.bind('skos', skos)

parser = argparse.ArgumentParser()
parser.add_argument('-i','--id', help='Resource Id', required=False)
parser.add_argument('-t', '--type', help='Convert resource to a specific format',choices=['xml', 'n3', 'turtle'], required=True)
args = parser.parse_args()

output_file = ''
output_fileName = ''
output_fileExtension =''

if (args.id):
    resource_url = endpoint + str("/" + str(args.id))
    output_fileName = "item_" + str(args.id)
else:
    resource_url = endpoint + str("/")
    output_fileName = 'all'

page = urllib.request.urlopen(resource_url)
resource_content = page.read().decode('utf-8')

data = json.loads(resource_content)

for element in data: 
    try:
        if('PinaDataTypes' in data[element][0]['type']):    
            del data[element][0]
    except Exception as e:
        continue

data = json.dumps(data)
data = data.replace('o:label','skos:prefLabel')

#print(data)
g = graph.parse(data=data, format='json-ld')

if (args.type == 'xml'):
    output_file = g.serialize(format='pretty-xml', indent=4).decode('utf-8')
    output_fileExtension = 'xml'
if (args.type == 'nt'):
    output_file = g.serialize(format='n3', indent=4).decode('utf-8')
    output_fileExtension = 'nt'
if (args.type == 'turtle'):
    output_file = g.serialize(format='turtle', indent=4).decode('utf-8')
    output_fileExtension = 'ttl'

f = open("output/" + output_fileName + "." + output_fileExtension, "w")
f.write(output_file)
f.close()
