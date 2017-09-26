import requests
 
url = 'http://httpbin.org/ip'

for i in range(50):
	print("{}: {}".format(i, requests.get(url).text))
	
#record program run time