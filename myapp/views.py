from urllib.request import urlretrieve, URLopener

import requests
from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    start = 495
    end = 500
    k = 1
    API1 = requests.get('https://api.coingecko.com/api/v3/coins/list')
    data1 = API1.json()
    for item in data1:
        if k >= start:
            print(item['id'])
            API2 = requests.get('https://api.coingecko.com/api/v3/coins/' + item['id'])
            data2 = API2.json()
            image = data2['image']
            image_large_url = image['large']
            # urlretrieve(image_large_url, item['id']+".jpg")
            opener = URLopener()
            opener.addheader('User-Agent', 'whatever')
            filename, headers = opener.retrieve(image_large_url, 'media/' + item['id'] + ".jpg")
        if k == end:
            break
        k += 1
    return HttpResponse('<h1>This is Http GET request.</h1>')
