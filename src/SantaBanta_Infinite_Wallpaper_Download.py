import os
from bs4 import BeautifulSoup
import urllib2

#query = input("Enter your search query")


# print(soup.prettify()) #BeautifulSoup function to print html documents
path = "E:\\Summertime Coding\\python\\wallpaper_downloader\\"
if not os.path.exists(path):
    os.makedirs(path)
def downloader(soup):
    for link in soup.find_all('img'):
        if(link.get('id')=="wall"):
            img_link=link.get('src')
            c = img_link.split('/')[-1]
            print "Downloading : ", img_link
            headers = { 'User-Agent' : 'Mozilla/5.0' }
            down = urllib2.Request(img_link, None, headers)
            resource = urllib2.urlopen(down)
            s=c
            s = os.path.join(path, s)
            print "Saving {0} to location : {1}".format(c,s)
            output = open(s,'wb')
            data1 = resource.read()
            output.write(data1)
            output.close()
    for link in soup.find_all('a'):
        if(link.get('id')=="wall_next"):
            link_next=link.get('href')
            link_next="http://santabanta.com"+link_next
            print "Requesting Next URL : " ,link_next
            headers = { 'User-Agent' : 'Mozilla/5.0' }
            req = urllib2.Request(link_next, None, headers)
            r = urllib2.urlopen(req)  # request package: use it to request any url.
            data = r.read()
            soup_fn = BeautifulSoup(data)
            downloader(soup_fn)
url=raw_input("Enter first URL : ")
print "First url: " ,url
headers = { 'User-Agent' : 'Mozilla/5.0' }
url = urllib2.Request(url, None, headers)
r = urllib2.urlopen(url)  # request package: use it to request any url.

data = r.read()
soup_global = BeautifulSoup(data)
downloader(soup_global)