from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
  return HttpResponse("Hello, World!")

def andrei(request):
  return HttpResponse("Hello, Andrei!")

def greet(request, name):
  return HttpResponse(f"Hello, {name}")