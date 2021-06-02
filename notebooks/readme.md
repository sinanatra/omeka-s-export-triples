## Introduction

A set of notebooks to convert a series of (custom) xml files to json-ld using CIDOC-CRM as vocabularies. 
It uses the Omeka-S api, as this is used as a CMS to store these semantic resources. 

These scripts are used to transform approximately 600 xml describing the "Lipperheidesche Kostümbibliothek", into rdf.

## Usage 

1. First obtain an api key.

2. Then run `import.ipynb` to import the ids of each resource.

3. Then import images `import_images.ipynb` and people `import_person.ipynb`.

4. Finally update the main resources with `update_items.ipynb`. This notebook should be run last, as it depends on the previous ones.