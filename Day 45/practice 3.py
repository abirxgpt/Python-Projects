from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

article = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
article_scores = []
for i in article:
    text = i.getText()
    article_texts.append(text)
    link = i.find("a").get('href')
    article_links.append(link)

ids = soup.find_all(name='tr', class_='athing submission')
for i in ids:
    article_id = i.get("id")
    score = soup.find(name='span', id=f'score_{article_id}').getText().split()
    article_scores.append(int(score[0]))

# print(article_texts)
# print(article_links)
# print(article_scores)

maximum_votes = max(article_scores)
indecs = article_scores.index(maximum_votes)
print(article_texts[indecs])
print(article_links[indecs])
print(article_scores[indecs])