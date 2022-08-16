from django.core.management.base import BaseCommand, CommandError
from newsapi import NewsApiClient
from main.models import Article

class Command(BaseCommand):
    help = 'My custom startup command, saving articles to local database'

    def handle(self, *args, **kwargs):
        try:
            # put startup code here
            newsapi = NewsApiClient(api_key='3fc9c2250b8a424f953f0f12f18a6019')
            headlines = newsapi.get_top_headlines(
                sources='bbc-news,the-verge'
            )
            articles = headlines['articles']
            for i in range(len(articles)):
                article = articles[i]
                articles_data = Article(
                    title=article['title'],
                    description=article['description'],
                    url_to_image=article['urlToImage'],
                    published_at= article['publishedAt'],
                    author=article['author'],
                    content=article['content'],
                )
                articles_data.save()
        except:
            raise CommandError('Initalization failed.')
