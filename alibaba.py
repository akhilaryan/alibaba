import requests
from bs4 import BeautifulSoup

baba = requests.get('http://sourcing.alibaba.com/rfq_search_list.htm?&availability=Y&openTime=7i').content
baba_bs = BeautifulSoup(baba)

mydivs = baba_bs.find_all("div", { "class" : "item-title" })
print mydivs