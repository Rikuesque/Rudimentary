import requests
from bs4 import BeautifulSoup

x = requests.get('https://news.ycombinator.com/')
stew = BeautifulSoup(x.text, 'lxml')

ls = []
matches = []
keyword = input("Enter a keyword to look for: ")

for messages in stew.find_all(class_="title"):
    something = messages.find('a')
    if something:
        ls.append(something.contents[0])

for i in ls:
    if keyword in i:
        matches.append(i)

print(matches)
