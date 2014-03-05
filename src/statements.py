import xml.etree.ElementTree as ET
from urllib2 import urlopen
from fileio import process_pdf
from util import date_f

class Statement:
    def __init__(self, date, title, author, publisher, id, content):
        self.date = date.encode('utf-8')
        self.title = title.encode('utf-8')
        self.author = author.encode('utf-8')
        self.publisher = publisher.encode('utf-8')
        self.id = id
        self.content = content # content is already encoded by pdfminer
        
    def __str__(self):
        str = "[Job: {date: " + self.date + ", title:" + self.title + \
              ", author: " + self.author + ", publisher:" + self.publisher + "}\n"
        return str
        #return str.encode('utf-8')




class StatementExtractor:

    NP_G = "{http://www.w3.org/1999/xhtml}"
    NP_E = "{http://di.tamu.edu/DRI/1.0/}"

    def extract(self, url):
        """
        extract from the collection page meta info of the statement and produce a statement object
        """
        tree = ET.parse(urlopen(url))   #Parse the first page
        root = tree.getroot()

        # Find the citation section of the page
        section = root.find(".//" + self.NP_G + "body/" + self.NP_G + "div[@id='page']//" +
                             self.NP_E + "div[@id='citation']")

        # Extract meta info from the citation section of the page
        author = section.find(self.NP_E + "span[@class='author']").text
        title = section.find(self.NP_E + "span[@class='title']").text
        publisher = section.find(self.NP_E + "span[@class='publisher']").text
        #date = section.find(self.NP_E + "span[@class='date']").text
        date = root.find(".//" + self.NP_G + "meta[@name='citation_date']").attrib['content']
        pdf_url = root.find(".//" + self.NP_G + "meta[@name='citation_pdf_url']").attrib['content']
        content = process_pdf(pdf_url)

        return Statement(date_f(date), title, author, publisher, "", content)
