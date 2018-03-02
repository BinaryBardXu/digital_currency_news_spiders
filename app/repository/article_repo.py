from . import mongo_client
import logging

logger = logging.getLogger(__name__)

articles_collection = 'articles'


def save(article):
    article_count = mongo_client.collection(articles_collection).find({"$or": [
        {"link": article['link']},
        {"title": article['title']}
    ]}).count()

    if article_count > 0:
        return

    mongo_client.collection(articles_collection).insert_one(article)
    logger.info('已入库新的数据')
    logger.info(article)
