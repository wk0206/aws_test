from django.shortcuts import render
from django.http import HttpResponse,Http404
from article.models import Article
from datetime import datetime

# Create your views here.
def home(request):
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list': post_list})

def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        return Http404
    return render(request, 'post.html', {'post' : post})

def category(request, cate):
    try:
        category_list = Article.objects.get(category=cate)
    except Article.DoesNotExist:
        return Http404
    return render(request, 'category.html', {'category_lsit' :category_list})


def test(request) :
    return render(request, 'test.html', {'current_time': datetime.now()})