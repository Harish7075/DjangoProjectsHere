from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import datetime as d 
def timeinfo(request):
    date=d.datetime.now()
    m='<h1>Hi Django Learners '
    t=int(date.strftime("%H"))
    if t<12:
        m=m+' Good morning all <hr>Now time is : '+str(date)+' </h1>'
        return HttpResponse(m)
    elif t<16:
        m=m+'Good Afternoon all <hr>Now time is : '+str(date)+' </h1>'
        return HttpResponse(m)
    elif t<21:
        m=m+'Good morning all <hr>Now time is : '+str(date)+' </h1>'
        return HttpResponse(m)
    else:
        m=m+'Good Night all<hr> Now time is : '+str(date)+' </h1>'
        return HttpResponse(m)

    
