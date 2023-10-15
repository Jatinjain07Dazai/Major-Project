from django.shortcuts import render
import json
import os
import nmap
import time, asyncio
from asgiref.sync import sync_to_async
from .Thread import Scanners
from django.http import HttpResponse
from .models import *

def Landing(request):
	return render(request, "index.html", {})


def result(request):
	start = time.time()
	url = request.GET['text']
	url = url[8:]
	os.chdir(os.getcwd()+ "/../spidey/")
	os.system("scrapy crawl stack -a " + "urls=https://builtwith.com/?https%3a%2f%2f" + url)
	with open("./../Cypher/cage/data.json", "r") as f:
		data = json.load(f)
		f.close()
	os.remove("./../Cypher/cage/data.json")
	Scanners(url).start()
	end = time.time()
	print(end - start)
	return render(request, "result.html", { "data": data, "url": url })


def result2(request):
	sub = {}
	with open("sub.txt", 'r') as f:
		for l in f:
			sub[str(l[:-1])] = "UP" 
	os.remove("sub.txt")
	with open("nscan.json", 'r') as f:
		nres = json.load(f)
		f.close()
	os.remove("nscan.json")
	nres = nres[list(nres.keys()).pop()]
	nres["subdomain"] = sub
	lists = [ k for k, v in nres.items() if (type(v) == list and v != [])]
	dicts = [ k for k, v in nres.items() if (type(v) == dict and v != {})]
	return render(request, "result2.html", {'nres': nres, 'lis':lists })


def vulnrecord(request):
	print(os.getcwd())
	with open('../Cypher/cage/vul.json', 'r') as fi:
		data = json.load(fi)
		fi.close()
	return render(request, "va.html", data)





def signal(request):
	try:
		with open("sub.txt", 'r') as f:
			f.close()
		return HttpResponse()
	except:
		return HttpResponse( status=404)

