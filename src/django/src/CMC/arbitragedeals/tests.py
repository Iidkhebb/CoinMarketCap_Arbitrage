from django.test import TestCase
from .models import AbitrageDeals

class AbitrageDealsTestCase(TestCase):
    def setUp(self):
        self.deal = AbitrageDeals.objects.create(
            token_name="Bitcoin",
            display_name="BTC",
            diff="10.0",
            blockchain="Bitcoin",
            address="0x123",
            exchangeName_low="ExchangeA",
            exchangeName_high="ExchangeB",
            marketpair_low="BTC/USD",
            marketpair_high="BTC/ETH",
            price_low="50000.0",
            price_high="51000.0",
            volumeusd_low="100000.0",
            volumeusd_high="200000.0",
            liquidy_score_low="0.5",
            liquidy_score_high="0.6",
            audit="Passed",
            dextoolslink="https://dextools.io",
            tokensnifferlink="https://tokensniffer.com",
            img_path="https://example.com/image.jpg",
            exchangeName_low_link="https://exchangea.com",
            exchangeName_high_link="https://exchangeb.com"
        )

    def test_deal_creation(self):
        """Test that a deal can be created"""
        self.assertIsInstance(self.deal, AbitrageDeals)

    def test_deal_string_representation(self):
        """Test that the deal string representation is correct"""
        self.assertEqual(str(self.deal), "BTC")

    def test_deal_fields(self):
        """Test that all fields are saved correctly"""
        self.assertEqual(self.deal.token_name, "Bitcoin")
        self.assertEqual(self.deal.display_name, "BTC")
        self.assertEqual(self.deal.diff, "10.0")
        self.assertEqual(self.deal.blockchain, "Bitcoin")
        self.assertEqual(self.deal.address, "0x123")
        self.assertEqual(self.deal.exchangeName_low, "ExchangeA")
        self.assertEqual(self.deal.exchangeName_high, "ExchangeB")
        self.assertEqual(self.deal.marketpair_low, "BTC/USD")
        self.assertEqual(self.deal.marketpair_high, "BTC/ETH")
        self.assertEqual(self.deal.price_low, "50000.0")
        self.assertEqual(self.deal.price_high, "51000.0")
        self.assertEqual(self.deal.volumeusd_low, "100000.0")
        self.assertEqual(self.deal.volumeusd_high, "200000.0")
        self.assertEqual(self.deal.liquidy_score_low, "0.5")
        self.assertEqual(self.deal.liquidy_score_high, "0.6")
        self.assertEqual(self.deal.audit, "Passed")
        self.assertEqual(self.deal.dextoolslink, "https://dextools.io")
        self.assertEqual(self.deal.tokensnifferlink, "https://tokensniffer.com")
        self.assertEqual(self.deal.img_path, "https://example.com/image.jpg")
        self.assertEqual(self.deal.exchangeName_low_link, "https://exchangea.com")
        self.assertEqual(self.deal.exchangeName_high_link, "https://exchangeb.com")
