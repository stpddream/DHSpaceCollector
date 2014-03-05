__author__ = 'stpanda'

import xml.etree.ElementTree as ET
from urllib2 import urlopen
from urllib2 import HTTPError

class CollectionPages:

    # name spaces
    GLOBAL_NP = '{http://www.w3.org/2005/Atom}'
    OS_NP = '{http://a9.com/-/spec/opensearch/1.1/}'

    def __init__(self, url):
        self.url = url
 
        tree = ET.parse(urlopen(url))   #Parse the first page
        total_results = int(tree.find(self.OS_NP + 'totalResults').text)

        print 'total results', total_results

        per_page = int(tree.find(self.OS_NP + 'itemsPerPage').text)
        self.total_pages = total_results / per_page + 1
        self.current_page = 1
        self.iterator = tree.iterfind(self.GLOBAL_NP + 'entry')

        print 'total pages', self.total_pages

        self.counter = 0






    def __next_page(self):
        """
           Helper function that retrieves the next page of results
        """
        self.current_page = self.current_page + 1
        tree = ET.parse(urlopen(self.url + '&start=' + str(self.current_page)))
        self.iterator = tree.iterfind(self.GLOBAL_NP + 'entry')


    def __iter__(self):
        return self

    def next(self):
        """
        Next url in this collection
        """
        cur_item = None
        while cur_item == None:
            try:
                cur_item = self.iterator.next()
            except StopIteration:
                if self.current_page < self.total_pages:
                    self.__next_page()
                else: raise

        element = cur_item.find(self.GLOBAL_NP + 'link')

        return element.attrib['href']


class ContentChecker:

    @staticmethod
    def is_valid(url):
        """
        Check if the statement is valid to use
        """

        HAVERFORD_TOKEN = 'Haverford users only'
        INVALID_TOKENS = [HAVERFORD_TOKEN, "Site Intel", "SITE Institute"]
        content = urlopen(url).read()

        for token in INVALID_TOKENS:
            if token in content:
                return False
        return True








