"""
- query Wikidata for resources with ISSNs
- create an index of issn - wikidata id pairs
- save as pickle file
"""
import sys
import pickle

from rdflib import Graph, Literal, URIRef
from rdflib.namespace import RDF, SKOS
from rdflib.plugins.stores import sparqlstore

# pickle file for ISSN index
INDEX_FILE = 'data/wd_issn.pkl'

store = sparqlstore.SPARQLStore('https://query.wikidata.org/sparql')

rq = """
PREFIX bd: <http://www.bigdata.com/rdf#>
PREFIX wikibase: <http://wikiba.se/ontology#>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>

SELECT ?j ?issn
WHERE 
{
    ?j wdt:P236 ?issn .
}
"""

def dump_pickle(data, fname):
    with open(fname, 'wb') as outf:
        pickle.dump(data, outf)
    return True

def index_journals():
    issn_key = {}
    for row in store.query(rq):
        uri = row.j.toPython()
        print>>sys.stderr, uri
        issn = row.issn.toPython()
        issn_key[issn] = uri

    dump_pickle(issn_key, INDEX_FILE)


if __name__ == "__main__":
    index_journals()