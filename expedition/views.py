from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import ExpeditionForm
from django.contrib import messages
from .models import Seferler, Firma, Musteri
from django.contrib.auth.decorators import login_required
from time import gmtime, strftime


def Index(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')

@login_required(login_url = "user:login")
def Dashboard(request):
    expeditions = Seferler.objects.filter(sofor=request.user)
    context = {
        'expeditions':expeditions,
    }
    return render(request, 'dashboard.html', context)

@login_required(login_url = "user:login")
def addExpedition(request):
    form = ExpeditionForm(request.POST or None)

    if form.is_valid():
        expedition = form.save(commit=False)

        expedition.sofor = request.user
        expedition.save()
        messages.success(request,"Transfer başarıyla oluşturuldu.")
        return redirect('expedition:dashboard')

    return render(request,'addexpedition.html',{"form":form})

def Detail(request,id):
    #expedition = Seferler.objects.filter(id = id).first()
    expedition = get_object_or_404(Seferler, id=id)
    return render(request, 'detail.html',{"expedition":expedition})

@login_required(login_url = "user:login")
def UpdateExpedition(request, id):
    expedition = get_object_or_404(Seferler, id = id)
    form = ExpeditionForm(request.POST or None, request.FILES or None,instance=expedition)
    if form.is_valid():
        expedition = form.save(commit=False)
        expedition.sofor = request.user
        expedition.save()
        messages.success(request,"Transfer başarıyla güncellendi.")
        return redirect('expedition:dashboard')

    return render(request, 'update.html', {"form":form})

@login_required(login_url = "user:login")
def DeleteExpedition(request, id):
    expedition = get_object_or_404(Seferler, id = id)
    expedition.delete()
    messages.warning(request,'Transfer başarıyla silindi.')
    return redirect('expedition:dashboard')


def chart(request):
    veri = Seferler.objects.all()
    title_list = []
    fiyat_list = []
    firma_list = []
    sofor_pilot_list = []
    for i in veri:
        title_list.append(i.sefer_yeri)
        fiyat_list.append(i.ucret)
        firma_list.append(i.firma)
        sofor_pilot_list.append(i.sofor_pilot)
        
    context = {
        'sofor_pilot' : sofor_pilot_list,
        'firma' : firma_list,
        'sefer_yeri' : title_list,
        'ucret' : fiyat_list,
        }
    return render(request, 'chart.html',context)


@login_required(login_url = "user:login")
def firma_list(request, firma):
    expeditions = Seferler.objects.filter(firma=firma)
    context = {
        'expeditions':expeditions,
    }

    return  render(request, 'firma_list.html', context)

@login_required(login_url = "user:login")
def sefer_tarihi(request):
    expedition = strftime("%c", gmtime())
    context = {
        'expedition' : expedition,
    }
    return  render(request, 'layout.html', context)
