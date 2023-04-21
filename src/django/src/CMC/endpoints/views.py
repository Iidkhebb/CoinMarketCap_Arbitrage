from rest_framework.response import Response
from rest_framework.decorators import api_view
from tokens.models import Tokens, FeedBar
from arbitragedeals.models import AbitrageDeals
from .serializers import TokensSerializer, FeedBarSerializer, AbitrageDealsSerializer

@api_view(['GET'])
def getTokens(request):
	tokens = Tokens.objects.all()
	serializer = TokensSerializer(tokens, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def getTokensByTokenName(request, token_name):
	tokens = Tokens.objects.filter(token_name=token_name)
	serializer = TokensSerializer(tokens, many=True)
	return Response(serializer.data)

@api_view(['POST'])
def addToken(request):
	serializer = TokensSerializer(data=request.data)
	if serializer.is_valid():
		serializer.save()
	return Response(serializer.data)

@api_view(['POST'])
def deleteToken(request):
    tokens = Tokens.objects.filter(token_name=request.data.get('token_name'))
    for token in tokens:
        token.delete()
    return Response('Tokens deleted')


@api_view(['GET'])
def getFeedBar(request):
	feed = FeedBar.objects.all()
	serializer = FeedBarSerializer(feed, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def getAbitrageDeals(request):
	deals = AbitrageDeals.objects.all()
	serializer = AbitrageDealsSerializer(deals, many=True)
	return Response(serializer.data)