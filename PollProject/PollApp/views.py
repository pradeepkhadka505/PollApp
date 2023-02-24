from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
arr =['java', 'python', 'c','cplusplus','.net','php','javascript','sql','ruby','php','swift','scala']
globalcnt = dict()

def index(request):
    my_dict = {
        "arr":arr
    }
    return render(request, 'index.html', context=my_dict)

def getquery(request):
    q = request.GET['languages']
    if q in globalcnt:
        globalcnt[q] = globalcnt[q]+1
    else:
        #for first occurance 
        globalcnt[q] = 1
    my_dict ={
        "arr": arr,
        "globalcnt": globalcnt
    }
    return render(request, 'index.html', context=my_dict)
    