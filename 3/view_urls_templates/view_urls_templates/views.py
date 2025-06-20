from django.shortcuts import render

def withTemplates(request):
    return render(request, 'index.html')