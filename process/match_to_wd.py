"""
Match local CSV file to indexed Wikidata ISSNs
saved as issn - wikidata pairs in data/wd_issn.pkl.
"""

import csv
import pickle
import sys


def load_index():
    with open('data/wd_issn.pkl') as inf:
        data = pickle.load(inf)
    return data

wd_idx = load_index()

def match(issn, eissn):
    for isn in [issn, eissn]:
        if issn != "":
            wd = wd_idx.get(issn)
            if wd is not None:
                return wd

def main():
    """
    Check the WD index for each row.
    """
    matches = 0
    with open(sys.argv[2], 'wb') as csvfile:
        fields = ['wosid', 'title', 'issn', 'eissn', 'wikidata']
        jwriter = csv.DictWriter(csvfile, fieldnames=fields)
        jwriter.writeheader()
        with open(sys.argv[1]) as infile:
            for n, row in enumerate(csv.DictReader(infile)):
                issn = row.get('issn')
                eissn = row.get('eissn')
                wd = match(issn, eissn)
                row['wikidata'] = wd
                jwriter.writerow(row)
                if wd is not None:
                    matches += 1

    print
    print '-' * 25
    print "Total journals", n + 1
    print "Wikidata matches", matches
    print "Matches ", round(matches / float(n) * 100, 2), "%"
    print 



if __name__ == "__main__":
    main()