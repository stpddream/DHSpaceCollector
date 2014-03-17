from spaceio import CollectionPages
from spaceio import ContentChecker
from statements import StatementExtractor
from fileio import produce_csv
from urllib2 import HTTPError
from sys import exit

url = "http://triceratops.brynmawr.edu:8080/dspace/open-search/?query=%22*%22&scope=10066/4022"

ce = StatementExtractor()
outfile = open("statements.csv", "wb")    #out put file
statement_pages = None
try:
    statement_pages = CollectionPages(url)
except HTTPError:
    print "Invalid URL."
    exit(-1)


for page in statement_pages:
    print page
    if ContentChecker.is_valid(page):
        statement = ce.extract(page)
        print statement
        produce_csv(outfile, statement)
    else:
        print "Invalid."

outfile.close()





