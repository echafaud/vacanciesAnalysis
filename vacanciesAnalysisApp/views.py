from . import models
from django.shortcuts import render
from .services import responses

def getPage(request, page):
    page, content = responses.GetPage(page)
    if page:
        return render(request, f'vacanciesAnalysisApp/{page}', content)


def getIndexPage(request):
    return render(request, 'vacanciesAnalysisApp/index.html')
