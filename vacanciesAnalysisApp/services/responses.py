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
    return page, content


def GetBDay():
    return (pd.Timestamp.now().replace(day=1) + pd.offsets.BDay()).strftime("%Y-%m-%d")


pages = {
    'demand': ('demand.html', {'headings': models.StatisticsByYear._meta.get_fields()[1:],
                               'statisticsData': models.StatisticsByYear.objects.all()}),
    'geography': ('geography.html', {'salaryHeadings': models.SalaryStatisticsByArea._meta.get_fields()[1:],
                                     'ratioHeadings': models.RatioStatisticsByArea._meta.get_fields()[1:],
                                     'salaryStatisticsData': models.SalaryStatisticsByArea.objects.all(),
                                     'ratioStatisticsData': models.RatioStatisticsByArea.objects.all()}),
    'skills': ('skills.html',
               {'years': sorted(set(models.SkillsStatisticsByYear.objects.values_list('year', flat=True))),
                'skillsStatistics': models.SkillsStatisticsByYear.objects.all()}),
    'recent': ('recent.html',
               {'vacancies': DistributorVacancies().GetRecentVacancies(GetBDay()),
                'headings': ['Название вакансии', 'Описание вакансии', 'Навыки', 'Компания', 'Оклад',
                          'Название региона', 'Дату публикации вакансии']})
}
