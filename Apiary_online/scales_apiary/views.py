from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def main_page(request):
    return HttpResponse("<b>The main page of the site!!!</b>")
