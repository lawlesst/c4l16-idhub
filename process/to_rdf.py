"""
Create RDF from matched CSV.
"""

import sys
import csv

from rdflib import Graph, URIRef, Literal, Namespace
from rdflib.namespace import RDF, RDFS, OWL
from rdflib.resource import Resource

DATA = Namespace("http://example.org/data/journals/")
BIBO = Namespace("http://purl.org/ontology/bibo/")
LOCAL = Namespace("http://example.org/ontology/hub#")

class Journal(object):
    """
    http://stackoverflow.com/a/1639197/758157
    """
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            # Set empty strings to none
            if v == '':
                v = None
            setattr(self, k, v)

    def _uri(self):
        if self.wosid is None:
            import ipdb; ipdb.set_trace()
            raise Exception("No wosid")
        return DATA[self.wosid]

    def to_rdf(self):
        uri = self._uri()   
        g = Graph()
        jr = Resource(g, uri)
        jr.set(RDF.type, BIBO.Journal)
        jr.set(RDFS.label, Literal(self.title))
        jr.set(LOCAL.identifier, Literal(self.wosid))
        if self.issn is not None:
            jr.set(BIBO.issn, Literal(self.issn))
        if self.eissn is not None:
            jr.set(BIBO.eissn, Literal(self.eissn))
        if self.wikidata is not None:
            jr.set(OWL.sameAs, URIRef(self.wikidata))
        return g

def main():
    g = Graph()
    with open(sys.argv[1]) as csvfile:
        for row in csv.DictReader(csvfile):
            jrnl = Journal(row)
            if jrnl.wosid is None:
                continue
            g += jrnl.to_rdf()

    g.serialize(destination=sys.argv[2], format="turtle")

if __name__ == "__main__":
    main()