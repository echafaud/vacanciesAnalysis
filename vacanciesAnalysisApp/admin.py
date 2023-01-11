from django.contrib import admin

from vacanciesAnalysisApp import models

# Register your models here.

admin.site.register([models.StatisticsByYear,
                     models.SalaryStatisticsByArea,
                     models.RatioStatisticsByArea,
                     models.SkillsStatisticsByYear])
