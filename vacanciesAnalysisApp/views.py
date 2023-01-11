from . import models
from django.shortcuts import render

pages = {
    'demand': ('demand.html', {'headings': models.StatisticsByYear._meta.get_fields()[1:],
                               'statisticsData': models.StatisticsByYear.objects.all()}),
    'geography': ('geography.html', {'salaryHeadings': models.SalaryStatisticsByArea._meta.get_fields()[1:],
                                     'ratioHeadings': models.RatioStatisticsByArea._meta.get_fields()[1:],
                                     'salaryStatisticsData': models.SalaryStatisticsByArea.objects.all(),
                                     'ratioStatisticsData': models.RatioStatisticsByArea.objects.all()}),
    'skills': ('skills.html', {'years': sorted(set(models.SkillsStatisticsByYear.objects.values_list('year', flat=True))),
                               'skillsStatistics': models.SkillsStatisticsByYear.objects.all()})
}


def getPage(request, page):
    page, content = pages.get(page, None)
    if page:
        return render(request, f'vacanciesAnalysisApp/{page}', content)


def getIndexPage(request):
    return render(request, 'vacanciesAnalysisApp/index.html')
