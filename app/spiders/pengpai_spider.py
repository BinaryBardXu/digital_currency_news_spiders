# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup

import requests
from app.article import Article

import config
from app.spiders.spider import Spider

site_name = '澎湃新闻'
homePageUrl = 'http://www.thepaper.cn/channel_25951'
baseUrl = 'http://www.thepaper.cn/'


class PengpaiSpider(Spider):
    def run(self):
        super(PengpaiSpider, self).banner(site_name)

        news_list = load_news()
        for news in news_list:
            title = str(news.string)
            href = baseUrl + news['href']
            if any(keyword in title for keyword in config.keywords):
                new_article = Article(title, '', href, site_name)
                super(PengpaiSpider, self).save_to_repository(new_article)


def load_news():
    home_page_data = requests.get(homePageUrl)
    home_page_html = BeautifulSoup(home_page_data.text, "html.parser")
    news_elements = home_page_html.find(class_="newsbox")
    return news_elements.find_all('a', href=True)
