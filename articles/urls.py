from django.contrib import admin
from django.urls import path

from .views import fetch_articles, fetch_article_id, fetch_author_articles

app_name = "articles"
urlpatterns = [
    path('', fetch_articles, name="articles-list"),
    path('<int:id>', fetch_article_id, name="article-detail-id"),
    path('author/<author>',
         fetch_author_articles, name="author-articles")
]
