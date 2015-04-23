from django.shortcuts import render
from django.template import RequestContext, loader
from django.http import HttpResponse
# Create your views here.

def home(request):
    context = {}
    template = "home.html"
    return render(request, 'testsite/home.html', context)
