# -*- coding: utf-8 -*-
'''by sudo rm -rf http://imchenkun.com'''


class DoubanBookPipeline(object):
    def process_item(self, item, spider):
        info = item['price'].split(' / ')  # [法] 圣埃克苏佩里 / 马振聘 / 人民文学出版社 / 2003-8 / 22.00元
        item['name'] = item['name']
        item['price'] = info[-1]
        item['edition_year'] = info[-2]
        item['publisher'] = info[-3]
        return item