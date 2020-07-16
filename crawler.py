import urllib.request, urllib.parse, urllib.error # url library package
from bs4 import BeautifulSoup # beautiful soup package

# getting start-url from the user
url = input('enter seed: ')
url_list = list()
url_list.append(url)

# main loop - starts here
while True:

    for u in url_list:
        # getting urls and avoiding unnecessary errors
        try:
            destination = urllib.request.urlopen(u).read()
        except:
            continue

        # getting anchors and references
        bsoup_entry = BeautifulSoup(destination, 'html.parser')
        ls = bsoup_entry('a')

        if len(ls) < 1:
            continue
        for l in ls:
            print(l.get('href', None), ':', l.contents[0])
            url_list.append(l.get('href', None))
    break
