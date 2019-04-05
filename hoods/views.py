from django.shortcuts import render,redirect
from django.http  import HttpResponse
from django.http  import HttpResponse,Http404




def neighbor(request):
    return render(request, 'index.html')

def hoods_of_day(request):
    return render(request, 'all-hoods/index.html')
