from pymongo import MongoClient

class MongoDB:
    def __init__(self, config):
        self.config = config.config['yourmove.mongodb']

        attribute_list = ['url', 'database']

        for attribute in attribute_list:
            setattr(self, attribute, self.config[attribute])

        self.client = MongoClient(self.url)
        self.db = self.client[self.database]
