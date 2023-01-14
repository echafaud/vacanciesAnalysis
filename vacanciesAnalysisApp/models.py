from django.db import models


class StatisticsByYear(models.Model):
    publishedYear = models.IntegerField('Год')
    avgSalary = models.IntegerField('Средняя з/п всех вакансий')
    avgSalaryByVacancy = models.IntegerField('Средняя з/п специалиста по информационной безопасности')
    countVacancies = models.IntegerField('Количество всех вакансий')
    countVacancy = models.IntegerField('Количество вакансий специалистов по информационной безопасности')

    def __str__(self):
        return self.publishedYear

    class Meta:
        verbose_name = 'Статистика по году'
        verbose_name_plural = 'Статистика по годам'


class SalaryStatisticsByArea(models.Model):
    salaryAreaName = models.CharField('Регион', max_length=255)
    avgSalaryByArea = models.IntegerField('Уровень зарплат')

    def __str__(self):
        return self.salaryAreaName

    class Meta:
        verbose_name = 'Уровень зарплат в регионе'
        verbose_name_plural = 'Уровень зарплат по регионам'


class RatioStatisticsByArea(models.Model):
    countAreaName = models.CharField('Регион', max_length=255)
    ratioByArea = models.FloatField('Доля вакансий')

    def __str__(self):
        return self.countAreaName

    class Meta:
        verbose_name = 'Доля вакансий в регионе'
        verbose_name_plural = 'Доля вакансий по регионам'


class SkillsStatisticsByYear(models.Model):
    year = models.IntegerField('Год')
    skill = models.CharField('Навык', max_length=255)
    count = models.IntegerField('Количество')
    ratio = models.FloatField('Доля')

    def __str__(self):
        return self.year

    class Meta:
        verbose_name = 'Доля навыка в году'
        verbose_name_plural = 'Доля навыков по годам'
