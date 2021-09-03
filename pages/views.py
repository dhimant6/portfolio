from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home_view(request, *args, **kwargs):
    #return HttpResponse ("<h1>Hellow World </h1>")
    return render(request, "home.html", {})
def contact(request, *args, **kwargs):
    print(request.user)
    return render(request, "contact.html", {})
    #return HttpResponse("<h1>Contact - 8496505143</h1>")
def sample(request, *args, **kwargs):
    return render(request, "sample.html", {})
