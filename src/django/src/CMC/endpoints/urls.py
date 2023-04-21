from django.urls import path
from . import views

app_name = 'endpoints'

urlpatterns = [
    path('getToken', views.getTokens, name='getTokens'),
    path('addToken', views.addToken, name='addToken'),
    path('deleteToken', views.deleteToken, name='deleteToken'),
    path('getFeedBar', views.getFeedBar, name='getFeedBar'),
    path('getAbitrageDeals', views.getAbitrageDeals, name='getAbitrageDeals'),
    path('getTokenByTokenName/<str:token_name>', views.getTokensByTokenName, name='getTokenByTokenName'),
]
