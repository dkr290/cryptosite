from django.shortcuts import render
import requests
import json
# Create your views here.


def home(request):
    # Grab crypto pricing data

    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,BCH,XRP,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=EUR")
    price = json.loads(price_request.content)

    # Grab crypto news
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN") 
    api = json.loads(api_request.content)
    return render(request,'home.html', {'api': api, 'price':price})


def prices(request):
    if request.method == 'POST':
        quote = request.POST['quote']
        quote = quote.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms="+ quote +"&tsyms=EUR")
        crypto = json.loads(crypto_request.content)
        return render(request,'prices.html', {'quote': quote, 'crypto': crypto })

    else:
        notfound = "Enter the crypto Currency Symbol in the Search form above..."
        return render(request, 'prices.html', { 'notfound': notfound })