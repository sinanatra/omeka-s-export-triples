import enum
from utils.setup import *
from rdflib import Graph, Literal, Namespace, RDF, URIRef, plugin
from rdflib.serializer import Serializer
import argparse
import urllib.request
import urllib.parse
import json

graph = Graph()

# change the namespace uri
graph.bind('ecrm', 'http://erlangen-crm.org', replace=True)
graph.bind('skos', 'http://www.w3.org/2004/02/skos/core#', replace=True)

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--id', help='Resource Id', required=False)
parser.add_argument('-r', '--related', help='Export Related Items', choices=['true'], required=False)
parser.add_argument('-m', '--media', help='Media Id', required=False)
parser.add_argument('-t', '--type', help='Convert resource to a specific format',
                    choices=['xml', 'nt', 'turtle'], required=True)
args = parser.parse_args()

output_file = ''
output_fileName = ''
output_fileExtension = ''

params = urllib.parse.urlencode({
    'key_identity': client_id,
    'key_credential': client_secret
})

if args.id:
    resource_url = endpoint + str("items/" + str(args.id))
    output_fileName = "item_" + str(args.id)
    data = [json.loads(urllib.request.urlopen(resource_url + params).read().decode('utf-8'))]

    if args.related:
        for element in data:
            for key in list(element):
                try:
                    for each in element[key]:
                        if 'resource' in each['type']:
                            resource = [json.loads(urllib.request.urlopen(
                                    each['@id'] + params).read().decode('utf-8'))]
                            data = data + resource
                except:
                    continue

elif args.media:
    resource_url = endpoint + str("media/" + str(args.media))
    output_fileName = "media_" + str(args.media)
    data = [json.loads(urllib.request.urlopen(resource_url + params).read().decode('utf-8'))]
else:
    resource_url = endpoint + str("items?page=all")
    media_url = endpoint + str("media?page=all")
    output_fileName = 'all'
    
    items = json.loads(urllib.request.urlopen(
        resource_url + params).read().decode('utf-8'))

    media = json.loads(urllib.request.urlopen(
        media_url + params).read().decode('utf-8'))

    data = items + media

# Remove Omeka-S dictionary
for element in data.copy():
    for key in list(element):
        if 'o:' in key:
            del element[key]
        if '@type' in key:
            if element[key][0] == 'o:Item' or element[key][0] == 'o:Media':
                del element[key][0]


def createNestedJsonLd(data):
    nestedJson = {}

    for element in data:
        for key in list(element):
            nestedJson[key] = []
            for each in element[key]:
                try:
                    if 'nesteddatatype' in each['type']:
                        nestedJson[key].append(each['properties'])
                except:
                    continue
            
            if not nestedJson[key]:
               nestedJson.pop(key, None)



    for key in data[0].copy():
        try:
            if nestedJson[key]:
                data[0].pop(key, None)
                data[0][key] = nestedJson[key]
        except:
            continue
        

createNestedJsonLd(data)
# replace labels
data = json.dumps(data)
data = data.replace('o:label', 'skos:prefLabel')

g = graph.parse(data=data, format='json-ld')

if args.type == 'xml':
    output_file = g.serialize(format='pretty-xml', indent=4).decode('utf-8')
    output_fileExtension = 'xml'

if args.type == 'nt':
    output_file = g.serialize(format='nt').decode('utf-8')
    output_fileExtension = 'nt'

if args.type == 'turtle':
    output_file = g.serialize(format='turtle', indent=4).decode('utf-8')
    output_fileExtension = 'ttl'

if output_file != '':
    # change the uri, only for develop
    output_file = output_file.replace(
        'http://erlangen-crm.org', 'http://erlangen-crm.org/200717/')

    f = open("output/" + output_fileName + "." + output_fileExtension, "w")
    f.write(output_file)
    f.close()
