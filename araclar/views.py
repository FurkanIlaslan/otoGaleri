from django.shortcuts import render,redirect
from araclar.models import *

# Create your views here.
def index(request):
    son_eklenen_araclar = Araclar.objects.order_by('-id')[:6]
    context = {
        'araclarim': son_eklenen_araclar
    }
    return render(request, "index.html", context)

# ! Araçları Filtrelemek İçin;
from django.db.models import Q

def araclarim_view(request):
    araclarim = Araclar.objects.all()

    marka = request.GET.get('marka')
    model = request.GET.get('model')
    yakit_turu = request.GET.get('yakit_turu')
    vites_turu = request.GET.get('vites_turu')
    min_km = request.GET.get('min_km')
    max_km = request.GET.get('max_km')
    min_tl = request.GET.get('min_tl')
    max_tl = request.GET.get('max_tl')
    min_yil = request.GET.get('min_yil')
    max_yil = request.GET.get('max_yil')

    filters = Q()

    if marka:
        filters &= Q(marka__icontains=marka)
    if model:
        filters &= Q(model__icontains=model)
    if yakit_turu:
        filters &= Q(yakit__icontains=yakit_turu)
    if vites_turu:
        filters &= Q(vites__icontains=vites_turu)
    if min_km:
        filters &= Q(km__gte=min_km)
    if max_km:
        filters &= Q(km__lte=max_km)
    if min_tl:
        filters &= Q(fiyat__gte=min_tl)
    if max_tl:
        filters &= Q(fiyat__lte=max_tl)
    if min_yil:
        filters &= Q(yıl__gte=min_yil)
    if max_yil:
        filters &= Q(yıl__lte=max_yil)

    araclarim = araclarim.filter(filters)

    # Fiyatları formatlamak için filtreleme işleminden sonra bir döngü kullanarak formatlayabiliriz
    for i in araclarim:
        i.fiyat = '{:,.0f}'.format(i.fiyat)

    context = {
        'araclarim': araclarim,
    }
    return render(request, 'araclarimiz.html', context)


def araclar(request):
    araclarim = Araclar.objects.all()
    
    context = {
        'araclarim': araclarim
    }
    return render(request, 'araclarimiz.html', context)


def detay(request, aracId):
    arac = Araclar.objects.filter(id = aracId)
    exper = Ekspertiz.objects.filter(arac_id = aracId)
    donanim = Donanım.objects.filter(arac_id = aracId)

    context = {
        'arac': arac,
        'exper':exper,
        'donanim':donanim,
    }

    return render(request, 'detay.html', context)



def iletisim(request):
    return render(request, 'iletisim.html')