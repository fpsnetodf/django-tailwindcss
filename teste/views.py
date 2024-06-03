from django.shortcuts import render

# Create your views here.

def teste1(request):
    return render(request, "teste/home.html")
