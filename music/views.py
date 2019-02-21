from django.http import HttpResponse
from django.shortcuts import render



def index(request):
    dict={'insert':"HEllO"}
    return render(request,'music/index.html',context="dict")
