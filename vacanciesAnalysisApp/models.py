from django.db import models


# Create your models here.

class StatisticsByYear(models.Model):
    year = models.IntegerField('Год')
    avgSalary = models.IntegerField('Средняя з/п всех вакансий')
    avgSalaryByVacancy = models.IntegerField('Средняя з/п заданной вакансии')
    countVacancies = models.IntegerField('Количество всех вакансий')
    countVacancy = models.IntegerField('Количество вакансий по заданной вакансии')

    def __str__(self):
        return self.year

    class Meta:
        verbose_name = 'Статистика по году'
        verbose_name_plural = 'Статистика по годам'


class SalaryStaticsByArea(models.Model):
    area = models.CharField('Расположение', max_length=255)
    avgSalary = models.IntegerField('Уровень зарплат')

    def __str__(self):
        return self.area

    class Meta:
        verbose_name = 'Уровень зарплат в городе'
        verbose_name_plural = 'Уровень зарплат по городам'


class RatioStaticsByArea(models.Model):
    area = models.CharField('Расположение', max_length=255)
    ratio = models.IntegerField('Доля вакансий')

    def __str__(self):
        return self.area

    class Meta:
        verbose_name = 'Доля вакансий в городе'
        verbose_name_plural = 'Доля вакансий по городам'
