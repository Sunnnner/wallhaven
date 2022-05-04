# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

import scrapy
from scrapy.pipelines.images import ImagesPipeline


class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        wallpaper_url = item['wallpaper_url']
        yield scrapy.Request(wallpaper_url)

    def item_completed(self, results, item, info):
        return item
