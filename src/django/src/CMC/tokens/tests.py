from django.test import TestCase
from .models import Tokens, FeedBar

class TokensModelTestCase(TestCase):
    def setUp(self):
        self.token = Tokens.objects.create(
            token_name='bitcoin',
            display_name='Bitcoin',
            blockchain='Bitcoin',
            address='0x123abc',
            tokenID='123abc',
            audit='Passed',
            dextoolslink='https://www.dextools.io/',
            tokensnifferlink='https://tokensniffer.com/',
            img_path='/static/images/bitcoin.png',
        )

    def test_token_display_name(self):
        self.assertEqual(str(self.token), 'Bitcoin')

    def test_token_defaults(self):
        self.assertEqual(self.token.audit, 'Passed')
        self.assertEqual(self.token.img_path, '/static/images/bitcoin.png')

    def test_token_max_length(self):
        max_length = Tokens._meta.get_field('token_name').max_length
        self.assertEqual(max_length, 200)


    def test_token_update_timestamps(self):
        old_created = self.token.created
        old_updated = self.token.updated
        self.token.display_name = 'BTC'
        self.token.save()
        self.assertNotEqual(old_created, self.token.created)
        self.assertNotEqual(old_updated, self.token.updated)

class FeedBarModelTestCase(TestCase):
    def setUp(self):
        self.feed_bar = FeedBar.objects.create(
            cryptos='Bitcoin, Ethereum, Cardano',
            exchanges='Binance, Coinbase, Kraken',
            marketcap='2 trillion',
            volume='100 billion',
            dominance='60%',
            ethgas='80 gwei',
        )

    def test_feed_bar_defaults(self):
        self.assertEqual(self.feed_bar.cryptos, 'Bitcoin, Ethereum, Cardano')
        self.assertEqual(self.feed_bar.dominance, '60%')

    def test_feed_bar_max_length(self):
        max_length = FeedBar._meta.get_field('cryptos').max_length
        self.assertEqual(max_length, 200)
