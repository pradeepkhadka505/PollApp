from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def my_poll(request):
    return render(request, 'index.html')
