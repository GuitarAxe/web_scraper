import requests
from bs4 import BeautifulSoup
import os

orig_home_dir = os.getcwd()


def save_article():
    anchor = news_article.find_parent('article').find('a', {'data-track-action': 'view article'})
    title = anchor.text
    title_floor = title.replace(" ", "_").replace("?", "")
    article_link = anchor.get('href')
    request_2 = requests.get('https://www.nature.com' + article_link)
    soup_2 = BeautifulSoup(request_2.content, 'html.parser')
    content = soup_2.find('div', {'class': 'c-article-body u-clearfix'}).text.strip()
    file = open(title_floor + '.txt', 'w', encoding='utf-8')
    file.write(content)
    file.close()


def create_folder():
    dir_name = 'Page_' + str(real_page)
    os.chdir(orig_home_dir)
    os.mkdir(dir_name)
    os.chdir(os.path.join(orig_home_dir, dir_name))


try:
    number_of_pages = int(input('Number of pages:'))
    type_of_articles = str(input('Type of articles:'))
    url = 'https://www.nature.com/nature/articles?sort=PubDate&year=2020'

    for page in range(number_of_pages):
        real_page = page + 1
        payload = {'page': real_page}
        page_content = requests.get(url, params=payload).content
        soup = BeautifulSoup(page_content, 'html.parser')
        news_article_links = soup.find_all('span', {'class': 'c-meta__type'}, text=type_of_articles)

        create_folder()
        for news_article in news_article_links:
            save_article()

except Exception as e:
    print('The URL returned ' + e)
