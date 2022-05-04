from django.shortcuts import render

# Create your views here.


def documentation(request, *args, **kwargs):
    return render(request, "documentation/index.html")
