from django.http import HttpResponse
from django.utils.translation import gettext
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "home.html", {"title": "Home"})