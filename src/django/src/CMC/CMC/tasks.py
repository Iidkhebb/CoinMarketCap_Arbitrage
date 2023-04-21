from __future__ import absolute_import, unicode_literals
from celery import shared_task
from tokens import models as token_models
from arbitragedeals import models as abitrage_models
from .tools.getprices import Routine
from .tools.getbardata import Bar
from  datetime import datetime

@shared_task
def updatePrices():
    TokenModel = token_models.Tokens.objects.all()
    ArbitrageModel = abitrage_models.AbitrageDeals
    
    i = 0
    for object in TokenModel:
        if i == 250:# debug
            break# debug

        
        Inst = Routine(object)
        print(Inst.token_name)
        deal = Inst.getPrices()
        if deal is not None:
            model = ArbitrageModel()

            # check if deal token_name already exists and update it with new data
            token = ArbitrageModel.objects.filter(token_name=deal['token_name'])
            if token.exists():
                model = token
                for token in model:
                    token.delete()
                model = ArbitrageModel()

            model.token_name = deal['token_name']
            model.display_name = deal['display_name']
            model.price_low = deal['price_low']
            model.price_high = deal['price_high']
            model.diff = deal['diff']
            model.blockchain = deal['blockchain']
            model.address = deal['address']
            model.exchangeName_low = deal['exchangeName_low']
            model.exchangeName_high = deal['exchangeName_high']
            model.marketpair_low = deal['marketpair_low']
            model.marketpair_high = deal['marketpair_high']
            model.volumeusd_low = deal['volumeusd_low']
            model.volumeusd_high = deal['volumeusd_high']
            model.liquidy_score_low = deal['liquidy_score_low']
            model.liquidy_score_high = deal['liquidy_score_high']
            model.audit = deal['audit']
            model.dextoolslink = deal['dextoolslink']
            model.tokensnifferlink = deal['tokensnifferlink']
            model.img_path = deal['img_path']
            model.exchangeName_low_link = deal['exchangeName_low_link']
            model.exchangeName_high_link = deal['exchangeName_high_link']
            model.save()

            
        i += 1 # debug
    return f"Tokens Task completed at {datetime.now()}"

@shared_task
def updateBarFeed():
    BarFeedModel = token_models.FeedBar

    update = Bar().get_bar_info()

    if update is not None:
        # Check if the model instance exists
        model, created = BarFeedModel.objects.get_or_create(pk=1)
        
        # Update the model instance with the latest data
        model.cryptos = update['cryptos']
        model.exchanges = update['exchanges']
        model.marketcap = update['marketcap']
        model.volume = update['volume']
        model.dominance = update['dominance']
        model.ethgas = update['ethgas']
        
        model.save()

    return f"BarFeed Task completed at {datetime.now()}"

        
      