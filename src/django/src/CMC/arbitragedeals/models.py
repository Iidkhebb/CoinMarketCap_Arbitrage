from django.db import models

class AbitrageDeals(models.Model):
	token_name = models.CharField(max_length=200)
	display_name = models.CharField(max_length=200)
	diff = models.CharField(max_length=200)
	blockchain = models.CharField(max_length=200)
	address= models.CharField(max_length=200)
	exchangeName_low= models.CharField(max_length=200)
	exchangeName_high= models.CharField(max_length=200)
	marketpair_low= models.CharField(max_length=200)
	marketpair_high= models.CharField(max_length=200)
	price_low= models.CharField(max_length=200)
	price_high= models.CharField(max_length=200)
	volumeusd_low= models.CharField(max_length=200)
	volumeusd_high= models.CharField(max_length=200)
	liquidy_score_low= models.CharField(max_length=200)
	liquidy_score_high= models.CharField(max_length=200)
	audit= models.CharField(max_length=200)
	dextoolslink= models.CharField(max_length=200)
	tokensnifferlink= models.CharField(max_length=200)
	img_path= models.CharField(max_length=200)
	exchangeName_low_link = models.CharField(max_length=200)
	exchangeName_high_link = models.CharField(max_length=200)

	create_date = models.DateTimeField(auto_now_add=True)
	update_date = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.display_name