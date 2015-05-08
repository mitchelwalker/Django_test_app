from django.shortcuts import render

# Create your views here.

def ehome(request):
    if request.user.is_authenticated():
        user_id = "Mitch Using Context"
        context = {"user_id": request.user}
    else:
        context = {"user_id": "unknown"}
        
    template = 'ebase.html'
    return render(request, template, context)