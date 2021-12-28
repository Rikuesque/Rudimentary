import requests
from bs4 import BeautifulSoup

r = requests.get('https://lynne.oratory.com/')
soup = BeautifulSoup(r.text, "lxml")
 
for entry_story in soup.find_all(class_="entry"):
    print(entry_story.text)