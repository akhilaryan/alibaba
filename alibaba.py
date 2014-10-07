import requests
from bs4 import BeautifulSoup

baba = requests.get('http://sourcing.alibaba.com/rfq_search_list.htm?&availability=Y&openTime=7i').content
baba_bs = BeautifulSoup(baba)

for div in baba_bs.find_all("div", { "class" : "item-title" }):
	go = div.findAll('a')[0]
	for a in go:
		print a.attrs['href']
	# print a.text.strip(), '=>', a.attrs['href']
# linko = sed.find_all('a')
