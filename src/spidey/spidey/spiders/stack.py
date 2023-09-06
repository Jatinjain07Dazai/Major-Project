import scrapy
import json
import os


class StackSpider(scrapy.Spider):
    name = "stack"
    allowed_domains = ["builtwith.com"]
    start_urls = ["https://builtwith.com/", "https://builtwith.com/?https%3a%2f%2fscrapy.org%2f"]

    def __init__(self, urls=[], *args, **kwargs):
        self.start_urls = urls.split(',')
        super(StackSpider, self).__init__(*args, **kwargs)


    def parse(self, response):
        cards = response.css(".card")
        data  = {}
        for i in cards:
            data[i.css("h6::text").get()] = i.css(".text-dark::text").getall()

        
        with open('D:/college/7th Semester/Major Project/Spector/src/Cypher/cage/data.json', "w") as f:
            print(data)
            json.dump(data, f, indent = 4)

        yield scrapy.Request()

