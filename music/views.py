from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    dict={'insert_content':"HEllO"}
    return render(request,'index.html',context="dict")
