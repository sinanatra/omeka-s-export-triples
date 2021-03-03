from rdflib import Graph, plugin
from rdflib.serializer import Serializer
import argparse
import urllib.request
from utils.setup import *

parser = argparse.ArgumentParser()
parser.add_argument('-i','--id', help='Resource Id', required=False)
parser.add_argument('-t', '--type', help='Convert resource to a specific format',choices=['xml', 'n3', 'turtle'], required=True)
args = parser.parse_args()

output_file = ''
output_fileName = ''

if (args.id):
    resource_url = endpoint + str("/" + str(args.id))
    output_fileName = "item_" + str(args.id)
else:
    resource_url = endpoint + str("/")
    output_fileName = 'all'

page = urllib.request.urlopen(resource_url)
resource_content = page.read().decode('utf-8')
g = Graph().parse(data=resource_content, format='json-ld')

if (args.type == 'xml'):
    output_file = g.serialize(format='xml', indent=4).decode('utf-8')
if (args.type == 'n3'):
    output_file = g.serialize(format='n3', indent=4).decode('utf-8')
if (args.type == 'turtle'):
    output_file = g.serialize(format='turtle', indent=4).decode('utf-8')

f = open("output/" + output_fileName + "." + args.type, "w")
f.write(output_file)
f.close()
