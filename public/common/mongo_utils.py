#coding=utf-8
import pymongo
from urllib import parse
from config.basic_config import ConfigInit
from loguru import logger


class MongoModel:
    def __init__(self):
        self.db = self.connect_sql()

    def connect_sql(self):
        user = parse.quote_plus(ConfigInit.mongo_user)
        pw = parse.quote_plus(ConfigInit.mongo_pw)
        try:
            client = pymongo.MongoClient('mongodb://{}:{}@{}/'.format(user, pw, ConfigInit.mongo_ip))
            mongo_db = client['jimi-platform']
            logger.info('连接 jimi-platform 成功')
        except Exception as e:
            logger.info('连接数据库失败')

        return mongo_db

    def delete_customer(self, phone):
        db = self.db
        t_organization_account = db['t_organization_account']
        t_organization_info = db['t_organization_info']
        ser = {
            "phone": phone
        }
        t_organization_account.delete_one(ser)
        logger.info('删除 t_organization_account 表记录 {} 成功'.format(ser))
        t_organization_info.delete_one(ser)
        logger.info('删除 t_organization_info 表记录 {} 成功'.format(ser))

if __name__ == '__main__':
    MongoModel().delete_customer('13800138011')