from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world! This is my First home page.")