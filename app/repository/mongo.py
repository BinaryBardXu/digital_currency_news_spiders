from pymongo import MongoClient
import application

MONGO_URL = 'mongodb://%s:%s@%s:%s/%s?authSource=%s' % (application.config.MONGO_USER,
                                                        application.config.MONGO_PASSWORD,
                                                        application.config.MONGO_HOST,
                                                        application.config.MONGO_HOST_PORT,
                                                        application.config.MONGO_COLLECTION_NAME,
                                                        application.config.MONGO_AUTH_SOURCE)
client = MongoClient(MONGO_URL)

db = client.digital_currency_news
collection = db.articles


def save(article):
    if collection.find({"$or": [{"link": article['link']}, {"title": article['title']}]}).count() > 0:
        return
    collection.insert_one(article)
