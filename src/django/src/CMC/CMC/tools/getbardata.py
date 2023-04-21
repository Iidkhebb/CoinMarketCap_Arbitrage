import requests
from bs4 import BeautifulSoup

 
class Bar():
	def __init__(self):
		self.url = "https://coinmarketcap.com/"
		self.tab = []
		pass

	def get_bar_info(self):
		html = requests.get(self.url).content
		htmlParse = BeautifulSoup(html, 'html.parser')
		feed =  htmlParse.find('div', {"class" : "container"})

		for row in feed.find_all('a'):
			self.tab.append(format(row.text.replace("\xa0", " ")))
		save = {
			'cryptos' : self.tab[0],
			'exchanges' : self.tab[1],
			'marketcap' : self.tab[2],
			'volume' : self.tab[3],
			'dominance' : self.tab[4],
			'ethgas' : self.tab[5]
		}

		return save
