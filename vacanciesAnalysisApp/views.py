from . import models
from django.shortcuts import render

pages = {
    'demand': ('demand.html', {'headings': models.StatisticsByYear._meta.get_fields()[1:],
                               'statisticsData': models.StatisticsByYear.objects.all()}),
    'geography': ('geography.html', {'salaryHeadings': models.SalaryStaticsByArea._meta.get_fields()[1:],
                                     'ratioHeadings': models.RatioStaticsByArea._meta.get_fields()[1:],
                                     'salaryStatisticsData': models.SalaryStaticsByArea.objects.all(),
                                     'ratioStatisticsData': models.SalaryStaticsByArea.objects.all()}),
}


def getPage(request, page):
    page, content = pages.get(page, None)
    if page:
        return render(request, f'vacanciesAnalysisApp/{page}', content)


def getIndexPage(request):
    return render(request, 'vacanciesAnalysisApp/index.html')
