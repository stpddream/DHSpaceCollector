__author__ = 'stpanda'

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from urllib2 import urlopen
from StringIO import StringIO

def process_pdf(url):
    process(StringIO(urlopen(url).read()))



def process(file):
    parser = PDFParser(file)
    document = PDFDocument(parser)
    document.initialize("")
    if not document.is_extractable:
        return -1

    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    codec = 'utf-8'
    device = TextConverter(rsrcmgr, retstr, codec = codec, laparams = laparams)

    interpreter = PDFPageInterpreter(rsrcmgr, device)
    pagenos = set()

    for page in PDFPage.get_pages(file, pagenos, maxpages=0, password="", caching=True,
                                  check_extractable=True):
        interpreter.process_page(page)
        print 'haah'

    a = retstr.getvalue()

    print "Value", a
    return a

