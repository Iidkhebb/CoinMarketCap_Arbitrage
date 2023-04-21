from sys import exit
import requests
from time import sleep as wait
import time
from ratelimit import limits, RateLimitException, sleep_and_retry

class Routine():
    
	def __init__(self, object) -> None:
		self.object = object
		self.token_name = object.token_name
		self.price_low = 0
		self.price_high = 0
		self.diff = 0
		self.blacklistMarkets = []
	
	@sleep_and_retry
	@limits(calls=95, period=60)
	def rateLimiter(self, token):
		url = f"https://api.coinmarketcap.com/data-api/v3/cryptocurrency/market-pairs/latest?slug={token}&start=1&limit=1000&category=spot&sort=cmc_rank_advanced"
		while True:
			try:
				response = requests.get(url)
				return response
			except KeyboardInterrupt:
				raise
			except requests.exceptions.ConnectionError:
				print("Connection error - waiting 5 seconds before retrying")
				time.sleep(5)
			except Exception as e:
				print(f"Error: {e}")
				return None

	def getPrices(self):
		request = self.rateLimiter(self.token_name)
		if request is None:
			return None
		request = request.json()
		if int(request['status']['error_code']) != 0:
			return None
	
		markets = [r for r in request['data']['marketPairs']]

		filtred = self.filter_exchanges(markets)
	
		slice_low = sorted(filtred[:len(filtred)//2], key=lambda x: x['depthUsdPositiveTwo'], reverse=True)
		slice_high = sorted(filtred[len(filtred)//2:], key=lambda x: x['depthUsdNegativeTwo'], reverse=True)

		re = []
		try:
			if (len(slice_low) >= 1 and len(slice_high) >= 1):
				slice_low = self.match_market_pair(slice_low[0]['baseSymbol'], slice_low)
				slice_high = self.match_market_pair(slice_high[0]['baseSymbol'], slice_high)
				if (len(slice_low) < 1 or len(slice_high) < 1):
					return None
				best_deals = self.find_best_deals(slice_low, slice_high)
				slice_low = slice_low[best_deals[0]['index']]
				slice_high = slice_high[best_deals[0]['index']]
			
				self.price_low = format(slice_low['price'], '.30f')
				self.price_high = format(slice_high['price'], '.30f')
				self.diff = ((((float(self.price_high) / float(self.price_low))) * 100) - 100)
				re = [slice_low, slice_high]
				
		except Exception as e:
			print("ERREUR on best exchanges side : " + str(e))
			return None
		diff = self.diff
		
		if diff < 0 or len(re) < 2:
			return None
		deal = self.subcribe_deal(diff, re)
		if deal is None:
			return None
		return deal
	
	def subcribe_deal(self, diff, re):
		try:
			if diff > 1 and diff < 10000:
				return self.construct_response(diff, re)
		
		except Exception as e:
			print("ERREUR on subcribe_deal side : " + str(e))
			return None
		return None
		
	def filter_exchanges(self, markets):
		filtred = []
		DEX = ['PancakeSwap (V2)', 'ShibaSwap']
		for r in markets:
			if r['volumeExcluded'] != 1 and r['priceExcluded'] != 1 and r['outlierDetected'] != 1:
			
				if (int(r['depthUsdPositiveTwo']) > 1000 or int(r['depthUsdNegativeTwo']) > 1000):
					if float(r['marketReputation']) > 0.7 and int(r['effectiveLiquidity']) >= 80 :	
						filtred.append(r)
				if r['exchangeName'] in DEX:
					if r['volumeUsd'] > 15000:
						filtred.append(r)
		filtred.sort(key=lambda x: x['price'], reverse=False)
		if len(filtred) % 2 != 0:
			filtred.pop()
		return filtred
	
	def match_market_pair(self, base_symbol, silce):
		result = []
		usd_symbol = ['USD', 'USDT', 'USDC', 'BUSD', 'BTC', 'ETH', 'BNB']
		generated_pair  = [f'{base_symbol}/{i}' for i in usd_symbol]
		for r in silce:
			if r['marketPair'] in generated_pair:
				result.append(r)
		return result

	def find_best_deals(self, slice_low, slice_high):
		list_of_indexes = []
		for index,  (l, h) in enumerate(zip(slice_low, slice_high)):
			diff = self.cal_diff(l, h)
			list_of_indexes.append({'index': index, 'diff': diff})
			
		return sorted(list_of_indexes, key=lambda x: x['diff'], reverse=True)

	def cal_diff(self, l, h):
		price_low = format(l['price'], '.30f')
		price_high = format(h['price'], '.30f')
		diff = ((((float(price_high) / float(price_low))) * 100) - 100)
		return diff
	
	def construct_response(self, diff, re):
	
		save = {
			'token_name' : self.token_name,
			'display_name' : str(self.object.display_name),
			'diff' : round(diff, 2),
			'blockchain' : str(self.object.blockchain),
			'address' : str(self.object.address),
			'exchangeName_low' : re[0]['exchangeName'],
			'exchangeName_high' : re[1]['exchangeName'],
			'marketpair_low' : re[0]['marketPair'],
			'marketpair_high' : re[1]['marketPair'],
			'price_low' : self.fix_price(self.price_low) if "0" in self.price_low[0] else str(round(float(self.price_low), 2)),
			'price_high' : self.fix_price(self.price_high) if "0" in self.price_high[0] else str(round(float(self.price_high), 2)),
			'volumeusd_low' : float(str(round(float(re[0]['volumeUsd']), 2))),
			'volumeusd_high' : float(str(round(float(re[1]['volumeUsd']), 2))),
			'liquidy_score_low' : str(int(re[0]['effectiveLiquidity'])),
			'liquidy_score_high' : str(int(re[1]['effectiveLiquidity'])),
			'audit' : self.confidence_grade(self.object),
			'dextoolslink' : str(self.object.dextoolslink),
			'tokensnifferlink' : str(self.object.tokensnifferlink),
			'img_path': str(self.object.img_path),
			'exchangeName_low_link' : str(re[0]['marketUrl']),
			'exchangeName_high_link' : str(re[1]['marketUrl'])
		}
		return save
	
	def fix_price(self, string):
		i = 0
		while string[i] == "0" or string[i] == ".":
			i += 1
		return (string[0:i+4])
	
	def confidence_grade(self, obj):
		try:
			audit = float(str(obj.audit))
			if (audit >= 6):
				return "High"
			elif((audit >= 3 and audit <= 5)):
				return "Moderate"
			elif( (audit >= 0 and audit < 3)):
				return "Low"

		except:
			return "N/A"
		return "N/A"