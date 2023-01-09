# Generated by Django 4.1.5 on 2023-01-09 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RatioStaticsByArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=255, verbose_name='Расположение')),
                ('ratio', models.IntegerField(verbose_name='Средняя з/п')),
            ],
            options={
                'verbose_name': 'Количество вакансий в городе',
                'verbose_name_plural': 'Статистика количества вакансий по городам',
            },
        ),
        migrations.CreateModel(
            name='SalaryStaticsByArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=255, verbose_name='Расположение')),
                ('avgSalary', models.IntegerField(verbose_name='Средняя з/п')),
            ],
            options={
                'verbose_name': 'Статистика зарплат в городе',
                'verbose_name_plural': 'Статистика зарплат по городам',
            },
        ),
        migrations.CreateModel(
            name='StatisticsByYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('avgSalary', models.IntegerField(verbose_name='Средняя з/п всех вакансий')),
                ('avgSalaryByVacancy', models.IntegerField(verbose_name='Средняя з/п заданной вакансии')),
                ('countVacancies', models.IntegerField(verbose_name='Количество всех вакансий')),
                ('countVacancy', models.IntegerField(verbose_name='Количество вакансий по заданной вакансии')),
            ],
            options={
                'verbose_name': 'Статистика по году',
                'verbose_name_plural': 'Статистика по годам',
            },
        ),
    ]
