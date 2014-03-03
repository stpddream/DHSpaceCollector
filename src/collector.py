from spaceio import CollectionPages
from spaceio import ContentChecker
from statements import StatementExtractor
from fileio import produce_csv

url = "http://triceratops.brynmawr.edu:8080/dspace/open-search/?query=super&scope=10066/4022"
ce = StatementExtractor()
outfile = open("statements.csv", "wb")

statement_pages = CollectionPages(url)
for page in statement_pages:
    if ContentChecker.is_valid(page):
        statement = ce.extract(page)
        print statement
        produce_csv(outfile, statement)
    else:
        print "Invalid."

outfile.close()





