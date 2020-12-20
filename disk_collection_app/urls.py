from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('add_disk', views.add_disk),
    path('delete_disk/<int:id>' , views.delete_disk),
]
