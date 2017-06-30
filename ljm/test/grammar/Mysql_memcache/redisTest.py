#!/usr/bin/python
# -*- coding: utf-8 -*-

import redis

class redisTest():

    ip = "10.10.10.61"
    port = 6379

    def connRedis(self):
        try:
            r = redis.StrictRedis(host=self.ip, port=self.port)
            # r.append('ljm','ljm')
            r.set('ljm2','ljm')
            print  "ljm: ",r.get('ljm')
            print  "ljm2: ",r.get('ljm2')
        except Exception as e:
            print e

if __name__=="__main__":
    redisTest().connRedis()