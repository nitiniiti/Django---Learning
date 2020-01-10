from django.shortcuts import render
from .models import Article
from django.http import Http404
from django.db.models.query import QuerySet

# Create your views here.


def fetch_articles(request):
    articles = Article.objects.all()
    context = {
        'articles_list': articles
    }

    return render(request, "all_articles.html", context)


def fetch_article_id(request, id):
    try:
        article = Article.objects.get(id=id)
    except Article.DoesNotExist:
        raise Http404

    context = {
        'article': article
    }
    return render(request, 'article_detail.html', context)


def fetch_author_articles(request, author):
    try:
        articles = Article.objects.filter(author=author)
    except Article.DoesNotExist:
        print("Its coming here")
        raise Http404

    context = {
        'articles': articles,
        'author': author
    }
    return render(request, 'author_articles.html', context)


def fetch_authors(request):
    try:
        articles = Article.objects.all()
        newSet = set()
        for article in articles:
            newSet.add(article.author)

    except Article.DoesNotExist:
        print("Not data found")
        raise Http404
    context = {
        'articles': newSet
    }
    return render(request, 'authors.html', context)
