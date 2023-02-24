from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.

def index(request):

    arr =['java', 'python', 'c','cplusplus','.net','php','javascript','sql','ruby','php','swift','scala']
    my_dict = {
        "arr":arr
    }
    return render(request, 'index.html', context=my_dict)

def getquery(request):
    q = request.GET['languages']
    return HttpResponse(q)
    