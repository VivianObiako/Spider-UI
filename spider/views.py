from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return render(request, 'spider/index.html')
    # return HttpResponse('Hello World!')


def pages(request):
    return render(request, 'spider/pages.html')
    # return HttpResponse('Hello World!')