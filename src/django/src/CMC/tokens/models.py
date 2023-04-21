from django.db import models

class Tokens(models.Model):
	token_name = models.CharField(max_length=200)
	display_name = models.CharField(max_length=200)
	blockchain = models.CharField(max_length=200)
	address = models.CharField(max_length=200)
	tokenID = models.CharField(max_length=200)
	audit= models.CharField(max_length=200)
	dextoolslink= models.CharField(max_length=200)
	tokensnifferlink= models.CharField(max_length=200)
	img_path= models.CharField(max_length=200)
	
	created = models.DateTimeField(auto_now=True)
	updated = models.DateTimeField(auto_now=True)


	def __str__(self):
		return self.display_name

class FeedBar(models.Model):
	cryptos = models.CharField(max_length=200)
	exchanges = models.CharField(max_length=200)
	marketcap = models.CharField(max_length=200)
	volume = models.CharField(max_length=200)
	dominance = models.CharField(max_length=200)
	ethgas = models.CharField(max_length=200)

	def __str__(self):
		return self.cryptos