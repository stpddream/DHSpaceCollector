from spaceio import CollectionUrl

"""

url = "http://triceratops.brynmawr.edu:8080/dspace/open-search/?query=super&scope=10066/4022"

it = CollectionUrl(url)

for num in it:
    print num

"""

from spaceio import ContentChecker

print ContentChecker.is_valid('http://triceratops.brynmawr.edu/dspace/handle/10066/11132')

from fileprocessor import process_url

print process_url('http://triceratops.brynmawr.edu/dspace/bitstream/handle/10066/11132/ZAW20120511.pdf?sequence=1')


