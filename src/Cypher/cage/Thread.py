import threading
import json
import os
import nmap
from django.http import HttpResponse

class Scanners(threading.Thread):
	def __init__(self, url, stack=[]):
		self.stack = stack
		self.url = url
		threading.Thread.__init__(self)

	def run(self):
		try:
			print("Thread execution started")
			sc = nmap.PortScanner()
			url= self.url
			print(url)
			k = sc.scan(url, '1-1024', '-v -sS -sV -sC -A -O')
			print("done")
			with open('nscan.json', 'w') as f:
				json.dump(k['scan'], f, indent=4)
				f.close()
			word = ["Fastly", "Hotjar"]
			os.system("findomain.exe -t" + str(url) + " -u sub.txt")
			for w in word:
				os.system("scrapy crawl vulscan -a urls=https://nvd.nist.gov/vuln/search/results?form_type=Basic^&results_type=overview^&query="+ w +"^&search_type=all^&isCpeNameSearch=false")
			os.system('start "window title" cmd /k "cd "../../src/Cypher/cage/Enigma" && "deactivate" && "ingest.py" && "HuntGPT.py"')	
		except Exception as e:
			print(e)
