from redis import Redis
import json

with open('config.json') as config_file:
    config = json.load(config_file)


class RedisHelper(object):
    def __init__(self):
        self.key = 'REDIS_LIST'
        self.r = Redis(host=config['DEFAULT']['HOST'],
                       port=config['DEFAULT']['PORT'],
                       db=config['DEFAULT']['DB'])

    def delete_key(self):
        self.r.delete(self.key)

    def rpush_data(self, data):
        if len(data) > 1:
            self.r.rpush(self.key, *data)
        else:
            self.r.rpush(self.key, data)

    def lpush_data(self, data):
        self.r.lpush(self.key, data)

    def lpush_data_list(self, data):
        self.r.lpush(self.key, *data)

    def rpop_data(self):
        self.pop = self.r.rpop(self.key)
        if self.pop:
            return self.pop.strip()
        else:
            return None
