from django.shortcuts import render,HttpResponse
#from django.http  import HttpResponse

# Create your views here.

def test(request):
    return HttpResponse("This is the home page of my MIT project")