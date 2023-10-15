import threading
import json
import os
import nmap
from django.http import HttpResponse

class Scanners(threading.Thread):
	def __init__(self, url):
		self.url = url
		threading.Thread.__init__(self)

	def run(self):
		try:
			print("Thread execution started")
			sc = nmap.PortScanner()
			url= self.url[:-1]
			print(url)
			k = sc.scan(url, '1-1024', '-v -sS -sV -sC -A -O')
			print("done")
			with open('nscan.json', 'w') as f:
				json.dump(k['scan'], f, indent=4)
				f.close()
			os.system("findomain.exe -t" + str(url) + " -u sub.txt")

		except Exception as e:
			print(e)
