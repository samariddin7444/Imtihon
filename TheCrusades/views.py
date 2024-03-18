from django.shortcuts import render

from .models import Crusade

# Create your views here.


def index(request):
    yurishlar = Crusade.objects.all()
    # yurishlar_1 = yurishlar[1:6]
    # yurishlar_2 = yurishlar[6:]
    # yurishlar_3 = yurishlar[0]
    return render(request, 'HTML/index.html', context={'yurishlar': yurishlar})


def index2(request,pk):
    yurishlar = Crusade.objects.get(pk=pk)
    return render(request, 'HTML/index2.html',context={'yurishlar': yurishlar})







