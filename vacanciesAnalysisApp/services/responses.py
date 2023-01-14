# import os
# import sys
# import django
#
# if __name__ == '__main__':
#     BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#     sys.path.append(BASE_DIR)
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vacanciesAnalysis.settings")
#     django.setup()

import pandas as pd
from vacanciesAnalysisApp import models
from .distributorVacancies import DistributorVacancies


def GetPage(pageName):
    page, content = pages.get(pageName, None)
    return page, content()


def GetDemandContent():
    return {'headings': models.StatisticsByYear._meta.get_fields()[1:],
            'statisticsData': models.StatisticsByYear.objects.all()}


def GetGeographyContent():
    return {'salaryHeadings': models.SalaryStatisticsByArea._meta.get_fields()[1:],
            'ratioHeadings': models.RatioStatisticsByArea._meta.get_fields()[1:],
            'salaryStatisticsData': models.SalaryStatisticsByArea.objects.all(),
            'ratioStatisticsData': models.RatioStatisticsByArea.objects.all()}


def GetSkillsContent():
    return {'years': sorted(set(models.SkillsStatisticsByYear.objects.values_list('year', flat=True))),
            'skillsHeadings': models.SkillsStatisticsByYear._meta.get_fields()[2::2],
            'skillsStatisticsData': models.SkillsStatisticsByYear.objects.all()}


def GetRecentContent():
    return {'vacancies': DistributorVacancies().GetRecentVacancies(GetBDay()),
            'headings': ['Название вакансии', 'Описание вакансии', 'Навыки', 'Компания', 'Оклад',
                         'Название региона', 'Дату публикации вакансии']}


def GetBDay():
    return (pd.Timestamp.now().replace(day=1) + pd.offsets.BDay()).strftime("%Y-%m-%d")


pages = {
    'demand': ('demand.html', GetDemandContent),
    'geography': ('geography.html', GetGeographyContent),
    'skills': ('skills.html', GetSkillsContent),
    'recent': ('recent.html', GetRecentContent)
}
