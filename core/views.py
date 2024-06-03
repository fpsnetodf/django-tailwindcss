from django.shortcuts import render

# Create your views here.

def home(request):
    # nome = request.GET.get("nome")
    return render(request, "core/index.html")

def teste(request):
    return render(request, 'core/modelo.html')
