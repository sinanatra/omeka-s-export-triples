from utils.setup import *
import xml.etree.ElementTree as ET
import requests
import argparse
import json

parser = argparse.ArgumentParser()
parser.add_argument('-f','--filename', help='Filename of the item', required=True)
args = parser.parse_args()

root = ET.parse(args.filename).getroot()

object_id = ''
painting_dimension = ''
painting_material = ''
frame_dimension = ''
location = ''

for group in root.findall('family/group'):
    item = group.findall('item')
    
    for value in item:

        if(value.attrib['name'] == 'Sammlungsobjekt-ID'):
            object_id = value.text 
        
        if(value.attrib['name'] == 'Gemälde Maße max. (H x B x T in cm)'):
            painting_dimension = value.text 
            
        if(value.attrib['name'] == 'Gemälde Material'):
            painting_material = value.text 
            
        if(value.attrib['name'] == 'Rahmen Maße max. (H x B x T in cm)'):
            frame_dimension = value.text 
            
        if(value.attrib['name'] == 'Abteilung'):
            location = value.text 
            
postFields =  { 
    "dcterms:title": [
        {
            "type": "literal",
            "property_id": 1,
            "property_label": "Title",
            "is_public": 'true',
            "@value": object_id
        }
    ],
    "dcterms:description": [
        {
            "type": "literal",
            "property_id": 4,
            "property_label": "Description",
            "is_public": 'true',
            "@value": painting_dimension
        }
    ],
    "dcterms:format": [
        {
            "type": "literal",
            "property_id": 9,
            "property_label": "Format",
            "is_public": 'true',
            "@value": painting_dimension
        }
    ],
    "dcterms:identifier": [
        {
            "type": "literal",
            "property_id": 10,
            "property_label": "Identifier",
            "is_public": 'true',
            "@value": object_id
        }
    ],
    "edm:currentLocation": [
        {
            "type": "literal",
            "property_id": 271,
            "property_label": "Current Location",
            "is_public": 'true',
            "@value": location
        }
    ]
}


url = access_url
headers = {"Content-Type": "application/json"}
r = requests.post(url, data=json.dumps(postFields), headers=headers)
