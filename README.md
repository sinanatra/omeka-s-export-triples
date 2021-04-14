# Pina O. Tools 

This repository contains a series of scripts which convert the data from Pina O. a cms based on Omeka S, to specific vocabularies structured in XML/RDF and n-tripless.

It additionally imports batch of XML data into Pina O. as JSON-LD items. 


Requirements
----------

1. Clone this repository:
   * `$ git clone https://github.com/sinanatra/Pina-O-tools`
1. Change into the specific directory:
   * `$ cd Pina-O-tools`
1. Perform first-time setup:
   * `$ pip install -r requirements.txt`
1. Open `config/api.ini` and add your Omeka S id, secret and endpoint.

Import
----------

1. Use  the jupyter notebooks at `/notebooks` to import data into the Omeka S as JSON-LD instances.


Export
----------

1. Use `convert.py` to convert data from the Omeka S instance to specific formats. 

    You must define the format by adding the parameter `-t`:

    `$ python convert.py -t xml`. 

    You can add the parameter `-i` to export only a specific resource:

    `$ python convert.py  -t xml -i 1`. 