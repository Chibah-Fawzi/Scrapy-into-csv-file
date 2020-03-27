import requests
from bs4 import BeautifulSoup
import csv



headers = requests.utils.default_headers()
headers.update()

url = 'https://www.kijiji.ca/b-immobilier/grand-montreal/c34l80002'
r = requests.get(url)
s = BeautifulSoup(r.content, 'html.parser')
links = s.select('body div.title > a')
a = []


for link in links:
    url = link.get('href')    
    url = "https:/"+url
    a.append(url)


with open("links.csv", 'w', newline='') as myfile:
     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL, delimiter='\n')
     wr.writerow(a)