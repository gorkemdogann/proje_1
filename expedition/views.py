from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from .forms import ExpeditionForm
from django.contrib import messages
from .models import Seferler, Chart
from django.contrib.auth.decorators import login_required


def Index(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')

@login_required(login_url = "user:login")
def Dashboard(request):
    expeditions = Seferler.objects.filter(sofor=request.user)
    #firmalar = Seferler.objects.filter(firma = request.)
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


@login_required(login_url = "user:login")
def chart(request):
    veri = Chart.objects.all()
    title_list = []
    fiyat_list = []
    yas_list = []
    for i in veri:
        title_list.append(i.title)
        fiyat_list.append(i.fiyat)
        yas_list.append(i.yas)
    print(title_list)
    print(fiyat_list)
    context = {
        'title' : title_list,
        'fiyat' : fiyat_list,
        'yas' : yas_list
        }
    
    return render(request, 'chart.html',context)


@login_required(login_url = "user:login")
def firma_list(request, firma):
    expeditions = Seferler.objects.filter(firma=firma)
    context = {
        'expeditions':expeditions,
    }

    return  render(request, 'firma_list.html', context)

