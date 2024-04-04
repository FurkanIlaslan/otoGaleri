from django.shortcuts import render

# Create your views here.

def giris(request):
    return render(request, 'giris.html')


def kayit(request):
    return render(request, 'kayit.html')