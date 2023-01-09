from django.contrib import admin

from vacanciesAnalysisApp.models import StatisticsByYear, SalaryStaticsByArea, RatioStaticsByArea

# Register your models here.

admin.site.register([StatisticsByYear, SalaryStaticsByArea, RatioStaticsByArea])
