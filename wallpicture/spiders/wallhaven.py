import json

import scrapy

from wallpicture.items import WallpictureItem


class WallhavenSpider(scrapy.Spider):
    name = 'wallhaven'
    allowed_domains = ['wallhaven.cc']
    base_url = 'https://wallhaven.cc/search?categories=110&purity=100&atleast=3840x1600&topRange=6M&sorting=toplist&order=desc&page={}'
    offset = 2
    start_urls = [base_url.format(offset)]

    def parse(self, response):
        proxy = "https://127.0.0.1:8889"
        wallpapers = response.xpath('//a[@class="preview"]/@href').extract()
        for wallpaper in wallpapers:
            yield scrapy.Request(wallpaper, callback=self.parse_search, meta={'proxy': proxy})

    def parse_search(self, response):
        item = WallpictureItem()
        wallpaper_url = response.xpath('//img[@id="wallpaper"]/@src').extract_first()
        name = wallpaper_url.split('/')[-1]
        item['wallpaper_url'] = wallpaper_url
        item['wallpaper_name'] = name
        yield item

        self.offset += 1
        yield scrapy.Request(self.base_url.format(self.offset), callback=self.parse)

