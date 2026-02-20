from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
    return render(request, 'index.html')
    # return HttpResponse('hello world')

def blog(request, blog_id):
    return render(request, 'blog_detail.html', {'blog_id': blog_id})
