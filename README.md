
## Overview

Processing code and examples for Code4Lib 2016 presentation, "[Build Your Own Identity Hub](http://2016.code4lib.org/Build-your-own-identity-hub)".


### process

The process directory contains:

* `get_wikidata_issns.py` - retrieves all ISSNs from Wikidata and builds a local index
* `match_to_wd.py` - matches the local data in `data\journals.csv` to Wikidata.
* `to_rdf.py` - converts the matched data in `data\journals_matched.csv` to a basic RDF model.

### ldf

Running the LDF Server requires nodejs and npm. To run first install the dependencies:

`$ cd ldf`
`$ npm install`

To start the server run:

`$ node_modules/ldf-server/bin/ldf-server config.json 5000`

View the `config.json` file to see how the LDF server reads your triple file.

A `Procfile` is included that will allow you to run the server on Heroku.

