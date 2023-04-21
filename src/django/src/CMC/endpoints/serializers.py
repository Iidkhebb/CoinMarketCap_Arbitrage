from rest_framework import serializers
from tokens.models import Tokens, FeedBar
from arbitragedeals.models import AbitrageDeals

class TokensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tokens
        fields = '__all__'

class FeedBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedBar
        fields = '__all__'

class AbitrageDealsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbitrageDeals
        fields = '__all__'