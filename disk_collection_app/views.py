from django.shortcuts import render, redirect, HttpResponse
from .models import Disks

def index(request):
    return redirect('/home')

def home(request):
    context = {
        'disks_list': Disks.objects.all(),
    }
    return render(request, 'home.html', context)

def add_disk(request):
    
    if request.method == "POST":
        genres_list = request.POST.getlist('genres')
        Disks.objects.create(
            title=request.POST['title'],
            released_date=request.POST['released_date'],
            production=request.POST['production'],
            prod_type=request.POST['type_of'],
            genres=genres_list,
        )
        return redirect('/home')

def delete_disk(request, id):
    delete_disk = Disks.objects.get(id=id)
    delete_disk.delete()
    return redirect('/home')

def disk_info(request, id):
    context = {
        'disk': Disks.objects.get(id=id),
    }
    return render(request, 'disk_info.html', context)