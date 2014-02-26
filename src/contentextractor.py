import xml.etree.ElementTree as ET
from urllib2 import urlopen
from fileio import process_pdf

class StateEntry:
    def __init__(self, date, title, author, publisher, id, content):
        self.date = date
        self.title = title
        self.author = author
        self.publisher = publisher
        self.id = id
        self.content = content
        
    def __str__(self):
        str = "[Job: {date: " + self.date + ", title:" + self.title + \
              ", author: " + self.author + ", publisher:" + self.publisher + "}\n"
        str += self.content
        return str





class ContentExtractor:

    NP_G = "{http://www.w3.org/1999/xhtml}"
    NP_E = "{http://di.tamu.edu/DRI/1.0/}"


    def extract_content(self, url):
         tree = ET.parse(urlopen(url))   #Parse the first page
         root = tree.getroot()
         section = root.find(".//" + self.NP_G + "body/" + self.NP_G + "div[@id='page']//" +
                             self.NP_E + "div[@id='citation']")

         author = section.find(self.NP_E + "span[@class='author']").text
         title = section.find(self.NP_E + "span[@class='title']").text
         publisher = section.find(self.NP_E + "span[@class='publisher']").text
         date = section.find(self.NP_E + "span[@class='date']").text
         pdf_url = root.find(".//" + self.NP_G + "meta[@name='citation_pdf_url']").attrib['content']


         content = process_pdf(pdf_url)


         return StateEntry(date, title, author, publisher, "", content)