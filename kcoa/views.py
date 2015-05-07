from django.shortcuts import render

def testhome(request):
    context = {}
    template = "donotuser.html"
    return render(request, template, context)