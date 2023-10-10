# Omeka S export triples

This repository contains a series of scripts which convert data from the Omeka S api to XML/RDF, turtle and n-triples.

Requirements
----------

1. Clone this repository:
   * `$ git clone https://github.com/sinanatra/omeka-s-export-triples`
1. Change into the specific directory:
   * `$ cd omeka-s-export-triples`
1. Perform first-time setup:
   * `$ pip install -r requirements.txt`
1. Open `config/api.ini` and add your Omeka S id, secret and endpoint.


Export
----------

1. Use `convert.py` to convert data from the Omeka S instance to specific formats. 

    You must define the format by adding the parameter `-t`:

    `$ python convert.py -t xml`. 

    You can add the parameter `-i` to export only a specific resource:

    `$ python convert.py  -t xml -i 1`. 