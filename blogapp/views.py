from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    # return HttpResponse("Test string!!!!!!!1")
    return render(request,"main.html", {'testvar':"teststring2"})