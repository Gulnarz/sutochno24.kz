from suto_api import views
from django.urls import path

urlpatterns = [
    path('more_apartments/', views.get_apartments),
]
