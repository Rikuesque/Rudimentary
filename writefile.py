from bs4.dammit import html_meta
import requests
from bs4 import BeautifulSoup

r = requests.get('https://www.duskborn.com/posts/2021-aoc-zig/')
soup = BeautifulSoup(r.text, 'lxml')

with open('overwrite.txt', 'w') as w:
    for post_content in soup.find_all(class_='post-content'):
        if post_content: 
            # print(post_content.contents)
            # print(post_content.text)
            # break
            w.write(post_content.text)
