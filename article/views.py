from django.shortcuts import render
from django.http import HttpResponse,Http404
from article.models import Article
import datetime
from datetime import timedelta
import time

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
        category_list = Article.objects.filter(category=cate)
    except Article.DoesNotExist:
        return Http404
    return render(request, 'sublist.html', {'sublist' :category_list})

def dateGroup(request,date):
    try:
        date2 = datetime.datetime.strptime(date,"%Y%m%d")
        start = date2
        aDay = timedelta(days=1)
        end = start+aDay
        date_list = Article.objects.filter(date_time__range=(start,end))
    except Article.DoesNotExist:
        return Http404
    return render(request, 'sublist.html', {'sublist' :date_list})


def test(request) :
    return render(request, 'test.html', {'current_time': datetime.now()})