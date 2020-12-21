from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home', views.home),
    path('add_disk', views.add_disk),
    path('disk_info/<int:id>', views.disk_info),
    path('delete_disk/<int:id>' , views.delete_disk),
]