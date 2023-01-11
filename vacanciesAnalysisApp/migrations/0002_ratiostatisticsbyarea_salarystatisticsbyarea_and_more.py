# Generated by Django 4.1.5 on 2023-01-10 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vacanciesAnalysisApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatioStatisticsByArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=255, verbose_name='Расположение')),
                ('ratio', models.FloatField(verbose_name='Доля вакансий')),
            ],
            options={
                'verbose_name': 'Доля вакансий в городе',
                'verbose_name_plural': 'Доля вакансий по городам',
            },
        ),
        migrations.CreateModel(
            name='SalaryStatisticsByArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(max_length=255, verbose_name='Расположение')),
                ('avgSalary', models.IntegerField(verbose_name='Уровень зарплат')),
            ],
            options={
                'verbose_name': 'Уровень зарплат в городе',
                'verbose_name_plural': 'Уровень зарплат по городам',
            },
        ),
        migrations.CreateModel(
            name='SkillsStatisticsByYear',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(verbose_name='Год')),
                ('skill', models.CharField(max_length=255, verbose_name='Навык')),
                ('count', models.IntegerField(verbose_name='Количество')),
                ('ratio', models.FloatField(verbose_name='Доля')),
            ],
            options={
                'verbose_name': 'Доля навыка в году',
                'verbose_name_plural': 'Доля навыков по годам',
            },
        ),
        migrations.DeleteModel(
            name='RatioStaticsByArea',
        ),
        migrations.DeleteModel(
            name='SalaryStaticsByArea',
        ),
    ]
