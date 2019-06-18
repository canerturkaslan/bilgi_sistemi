from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from ogrenci.models import Notlar,Ogrenci,Dersler


def home_page(request):
    return render(request, 'home.html')


def add_not_page(request):

    if request.method == 'POST':

        model = {
            'ogrenci_id': request.POST['ogrenci_id'],
            'dersler_id': request.POST['dersler_id'],
            'puan': request.POST['puan'],

        }

        notlar=Notlar.objects.create(
            dersler_id=model['dersler_id'],
            puan=model['puan'],
            ogrenci_id=model['ogrenci_id'],

        )



    return render(request, 'add_page.html')

