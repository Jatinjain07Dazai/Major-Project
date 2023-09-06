from django.shortcuts import render
import json
import os

def Landing(request):
	return render(request, "index.html", {})


def result(request):
	url = request.GET['text']
	os.chdir(os.getcwd()+ "/../spidey/")
	os.system("scrapy crawl stack -a " + "urls=https://builtwith.com/?https%3a%2f%2f" + url[8:])
	with open("./../Cypher/cage/data.json", "r") as f:
		data = json.load(f)
	return render(request, "result.html", { "data" : data, "url" : url })