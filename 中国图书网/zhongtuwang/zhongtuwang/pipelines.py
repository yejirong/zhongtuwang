# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pandas as pd  # 导入库


class ZhongtuwangPipeline(object):

    def process_item(self, item, spider):
        data = pd.DataFrame(dict(item), index=[0])
        data.to_csv("./book.csv", mode='a+', index=None, header=None)  # 追加形式写入文件

        return item
