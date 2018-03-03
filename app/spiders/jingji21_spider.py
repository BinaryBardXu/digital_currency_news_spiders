# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

import requests
from app.article import Article

import config
from app.spiders.spider import Spider

site_name = '21世纪经济报道'
homePageUrl = 'http://www.21jingji.com/channel/finance/'


class Jingji21Spider(Spider):
    def run(self):
        super(Jingji21Spider, self).banner(site_name)

        news_list = load_news()
        for news in news_list:
            title = str(news.string)
            href = news['href']
            if any(keyword in title for keyword in config.keywords):
                new_article = Article(title, '', href, site_name)
                super(Jingji21Spider, self).save_to_repository(new_article)


def load_news():
    home_page_data = requests.get(homePageUrl)
    home_page_data.encoding = 'utf-8'  # 显式地指定网页编码，一般情况可以不用

    home_page_html = BeautifulSoup(home_page_data.text, "html.parser")
    news_elements = home_page_html.find(class_="contList")
    return news_elements.find_all('a', href=True)
