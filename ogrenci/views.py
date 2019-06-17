from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import NotForm
from ogrenci.models import Notlar


def home_page(request):
    return render(request, 'home.html')


def add_not_page(request,notlar_id):

    if request.method == 'GET':
        Notlar.objects.all()

    elif request.method == 'POST':

        form = NotForm(request.POST)

        if form.is_valid():
            ders_id = form.cleaned_data['ders_id']
            ogrenci_id = form.cleaned_data['ogrenci_id']
            puan = form.cleaned_data['puan']

            Notlar.objects.create(
                ders_id=ders_id,
                ogrenci_id=ogrenci_id,
                puan=puan
            )
    return render(request, 'add_page.html')

