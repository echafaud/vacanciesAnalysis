from django.shortcuts import render

pages = {
    'index': 'index.html',
    'main': 'base.html'
}


def getPage(request, page):
    page = pages.get(page, None)
    if page:
        return render(request, f'vacanciesAnalysisApp/{page}')


def getIndexPage(request):
    a = 1
    return render(request, 'vacanciesAnalysisApp/index.html')
