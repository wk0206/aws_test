from django.shortcuts import render
from django.http import HttpResponse,Http404
from article.models import Article
from datetime import datetime

# Create your views here.
def home(request):
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list': post_list})

def detail(request, parameter):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        return Http404
    return render(request, 'post.html', {'post' : post})


def test(request) :
    return render(request, 'test.html', {'current_time': datetime.now()})