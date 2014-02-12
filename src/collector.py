from spaceio import CollectionUrl


url = "http://triceratops.brynmawr.edu:8080/dspace/open-search/?query=super&scope=10066/4022"

it = CollectionUrl(url)

for num in it:
    print num






