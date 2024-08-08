from django.http import HttpResponse

def text(request):
    return HttpResponse("Hello, world! This is my custom text view.")
