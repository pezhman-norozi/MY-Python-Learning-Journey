import requests


r= requests.get("https://www.iranketab.ir")
print(r.status_code)

data = r.text

from bs4 import BeautifulSoup


soup = BeautifulSoup(data , "html.parser")

page_title = soup.title.text
print(page_title)

titles = soup.find_all(class_="swiper")
for i in titles:
    print(i.text.strip())

images = soup.find_all("img")
for img in images:
    print(img["src"])