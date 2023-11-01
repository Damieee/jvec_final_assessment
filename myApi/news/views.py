
from django.shortcuts import render
from .models import NewsItem
from celery import shared_task
import requests

from django.views.generic import ListView
from .models import NewsItem

class NewsListView(ListView):
    model = NewsItem

    def latest_news(requests):
        url = 'https://hackernews.api-docs.io'
        try:
            response = requests.get(url)

            if response.status_code == 200:

                data = response.json()  

                return data
            else:
                print("Request failed with status code:", response.status_code)

        except requests.RequestException as e:
            print("Request failed:", e)


