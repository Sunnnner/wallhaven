from scrapy import cmdline


name = "wallhaven"
cmd = f"scrapy crawl {name}"
cmdline.execute(cmd.split())
