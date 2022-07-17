from django.http import HttpResponse
from django.utils.translation import gettext
from django.shortcuts import redirect, render
from suto_api.models import Apartment
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        "title": "SUTOCHNO24.KZ"
    }
    apartments = Apartment.objects.filter(status="С")
    rooms = request.GET.get("rooms", 0)
    if rooms:
        if rooms == "1":
            room = "О"
            context["type"] = 1
        else: 
            room = "Д"
            context["type"] = 2
        all_obj = apartments.filter(type=room).all()
    else:
        all_obj = apartments.all()
    context["apartments"] = all_obj[:4]
    count = len(all_obj)
    if count > 4: context["has_next"] = True
    else: context["has_next"] = False
    return render(request, "home.html", context)

def details(request, name):
    context = {}
    apartment = Apartment.objects.filter(name=name).first()
    if not apartment:
        messages.add_message(request, messages.ERROR, "Apartment doesn't found")
        return redirect("/")
    context["title"] = apartment.address
    context["apartment"] = apartment
    return render(request, "details.html", context)