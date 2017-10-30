from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article

# Create your views here.
def home(request):
    return HttpResponse("test for parameter %s.")

def detail(request, parameter):
    post = Article.objects.all()[int(parameter)]
    str = ("title = %s, category = %s, date_time = %s, content = %s"
           %(post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)