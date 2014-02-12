import xml.etree.ElementTree as ET
from urllib2 import urlopen

class CollectionUrl:

    # name spaces
    GLOBAL_NP = '{http://www.w3.org/2005/Atom}'
    OS_NP = '{http://a9.com/-/spec/opensearch/1.1/}'

    #Base url
    COL_URL = 'http://triceratops.brynmawr.edu:8080/dspace/open-search/?scope=10066/4022'


    def __init__(self, url):
        self.url = url

        tree = ET.parse(urlopen(url))

        total_results = int(tree.find(self.OS_NP + 'totalResults').text)

        print 'total results', total_results

        per_page = int(tree.find(self.OS_NP + 'itemsPerPage').text)
        self.total_pages = total_results / per_page + 1
        self.current_page = 1
        self.iterator = tree.iterfind(self.GLOBAL_NP + 'entry')

        print 'total pages', self.total_pages

        self.counter = 0


    def __next_page(self):
        self.current_page = self.current_page + 1
        tree = ET.parse(urlopen(self.url + '&start=' + str(self.current_page)))
        self.iterator = tree.iterfind(self.GLOBAL_NP + 'entry')


    def __iter__(self):
        return self

    def next(self):

        cur_item = None

        while cur_item == None:
            try:
                cur_item = self.iterator.next()
            except StopIteration:
                if self.current_page < self.total_pages:
                    self.__next_page()
                else: raise

        element = cur_item.find(self.GLOBAL_NP + 'link')
        self.counter = self.counter + 1
        print self.counter

        return element.attrib['href']
