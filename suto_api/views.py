from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from suto_api.models import Apartment
from suto_api.serializers import ApartmentSerializer

# Create your views here.

@api_view(['GET'])
def get_apartments(request):
    page = int(request.GET.get("page", 1))
    rooms = int(request.GET.get("rooms", 0))
    has_next = False
    if rooms == 1:
        apartments_all = Apartment.objects.filter(type="О")
    elif rooms == 2:
        apartments_all = Apartment.objects.filter(type="Д")
    else:
        apartments_all = Apartment.objects.all()
    if page != 1:
        apartments = apartments_all[4+(page-2)*2:4+(page-2)*2+2]
        count = len(apartments_all)
        if count > 4+(page-2)*2+2:
            has_next = True
    serializer = ApartmentSerializer(apartments, many=True)
    data = {
        "apartments": serializer.data,
        "has_next": has_next
    }
    return Response(data)