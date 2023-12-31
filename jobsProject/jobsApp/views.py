from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hyderbadjobs(request):
    m='<h1>Hyderbad Jobs information<hr>Display in this page</h1>'
    return HttpResponse(m)

def punejobs(request):
    m='<h1>Pune Jobs information<hr>Display in this page</h1>'
    return HttpResponse(m)

def noidajobs(request):
    m='<h1>Noida Jobs information<hr>Display in this page</h1>'
    return HttpResponse(m)

def delhijobs(request):
    m='<h1>Delhi Jobs information<hr>Display in this page</h1>'
    return HttpResponse(m)