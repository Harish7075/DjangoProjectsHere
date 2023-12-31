from django.contrib import admin
from django.urls import path
from jobsApp import views
urlpatterns = [
    path('hyd/',views.hyderbadjobs),
    path('pune/',views.punejobs),
    path('noida/',views.noidajobs),
    path('delhi/',views.delhijobs)
]
