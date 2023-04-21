from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from tokens.models import Tokens, FeedBar
from arbitragedeals.models import AbitrageDeals
from endpoints.serializers import TokensSerializer, FeedBarSerializer, AbitrageDealsSerializer

class TestTokensViews(APITestCase):
    client = APIClient()

    @classmethod
    def setUp(cls):
        # create some tokens
        Tokens.objects.create(token_name='token1')
        Tokens.objects.create(token_name='token2')
        cls.getTokens_url = reverse('endpoints:getTokens')
        cls.getTokensByTokenName_url = reverse('endpoints:getTokenByTokenName', args=['token1'])
        cls.addToken_url = reverse('endpoints:addToken')
        cls.deleteToken_url = reverse('endpoints:deleteToken')
        cls.getFeedBar_url = reverse('endpoints:getFeedBar')
        cls.getAbitrageDeals_url = reverse('endpoints:getAbitrageDeals')

    def test_getTokens(self):
        response = self.client.get(self.getTokens_url)
        tokens = Tokens.objects.all()
        serializer = TokensSerializer(tokens, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getTokensByTokenName(self):
        response = self.client.get(self.getTokensByTokenName_url)
        tokens = Tokens.objects.filter(token_name='token1')
        serializer = TokensSerializer(tokens, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_addToken(self):
        data = {'token_name': 'token3', 
                'display_name': 'token3',
                'blockchain': 'Ethereum',
                'address': '0x000000',
                'tokenID': '498',
                'audit': 'https://www.google.com',
                'dextoolslink': 'https://www.google.com',
                'tokensnifferlink': 'https://www.google.com',
                'img_path': 'https://www.google.com',
        }
        response = self.client.post(self.addToken_url, data)
        token = Tokens.objects.get(token_name='token3')
        serializer = TokensSerializer(token)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(token.created)
        self.assertIsNotNone(token.updated)


    def test_deleteToken(self):
        data = {'token_name': 'token1'}
        response = self.client.post(self.deleteToken_url, data)
        self.assertEqual(response.data, 'Tokens deleted')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getFeedBar(self):
        response = self.client.get(self.getFeedBar_url)
        feed = FeedBar.objects.all()
        serializer = FeedBarSerializer(feed, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_getAbitrageDeals(self):
        response = self.client.get(self.getAbitrageDeals_url)
        deals = AbitrageDeals.objects.all()
        serializer = AbitrageDealsSerializer(deals, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
