import os
import sys
import django

if __name__ == '__main__':
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(BASE_DIR)
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vacanciesAnalysis.settings")
    django.setup()

import pandas as pd
from imgGenerator import Report
from __init__ import InitializeDB
from vacanciesAnalysisApp import models
from dataBase import DataBase as DB
from modelsRequester import InsertData

# convertedVacanciesDB, convertedVacanciesDF = InitializeDB()
convertedVacanciesDB = DB('convertedVacancies')
convertedVacanciesDB.OpenDB()
avgSalary = convertedVacanciesDB.GetResponseDF("""SELECT strftime('%Y', published_at) as publishedYear,
         CAST(AVG(salary) as INTEGER) as avgSalary 
         FROM convertedVacancies 
         GROUP BY publishedYear""").set_index('publishedYear')

avgSalaryByVacancy = convertedVacanciesDB.GetResponseDF(f"""SELECT strftime('%Y', published_at) as publishedYear,
         CAST(AVG(salary) as INTEGER) as avgSalaryByVacancy 
         FROM convertedVacancies 
         WHERE (LOWER(name) LIKE '%специалист по информационной безопасности%')
            OR (LOWER(name) LIKE '%безопасность%')
            OR (LOWER(name) LIKE '%защита%')
            OR (LOWER(name) LIKE '%information security specialist%')
            OR (LOWER(name) LIKE '%information security%')
            OR (LOWER(name) LIKE '%фахівець служби безпеки%')
            OR (LOWER(name) LIKE '%cyber security%')
         GROUP BY publishedYear""").set_index('publishedYear')

countVacancies = convertedVacanciesDB.GetResponseDF("""SELECT strftime('%Y', published_at) as publishedYear, 
        COUNT(name) as countVacancies
        FROM convertedVacancies
        GROUP BY publishedYear""").set_index('publishedYear')

countVacancy = convertedVacanciesDB.GetResponseDF(f"""SELECT strftime('%Y', published_at) as publishedYear,
        COUNT(name) as countVacancy
        FROM convertedVacancies 
        WHERE (LOWER(name) LIKE '%специалист по информационной безопасности%')
            OR (LOWER(name) LIKE '%безопасность%')
            OR (LOWER(name) LIKE '%защита%')
            OR (LOWER(name) LIKE '%information security specialist%')
            OR (LOWER(name) LIKE '%information security%')
            OR (LOWER(name) LIKE '%фахівець служби безпеки%')
            OR (LOWER(name) LIKE '%cyber security%')
        GROUP BY publishedYear""").set_index('publishedYear')

avgCitySalary = convertedVacanciesDB.GetResponseDF(f"""SELECT area_name as salaryAreaName, 
        CAST(AVG(salary) as INTEGER) as avgSalaryByArea
        FROM convertedVacancies 
        GROUP BY salaryAreaName HAVING 
        (CAST(COUNT(name) as REAL) / (SELECT COUNT(*) 
        FROM convertedVacancies) >= 0.01) 
        ORDER BY avgSalaryByArea 
        DESC LIMIT 10""")

avgCityCount = convertedVacanciesDB.GetResponseDF(f"""SELECT area_name as countAreaName, 
        ROUND(CAST(COUNT(name) as REAL) / (SELECT COUNT(*) 
        FROM convertedVacancies), 4) as ratioByArea 
        FROM convertedVacancies 
        GROUP BY countAreaName 
        HAVING (CAST(COUNT(name) as REAL) / (SELECT COUNT(*) 
        FROM convertedVacancies) >= 0.01) 
        ORDER BY ratioByArea 
        DESC LIMIT 10""")

years = convertedVacanciesDB.GetResponseDF(f"""SELECT DISTINCT year FROM Skills""")['year'].tolist()

skillsStatistics = pd.DataFrame()
for year in years:
    skillsStatistics = pd.concat([skillsStatistics, convertedVacanciesDB.GetResponseDF(f"""with Top as (SELECT year, skill, COUNT(skill) as count
        FROM Skills
        WHERE ((LOWER(vacancy) LIKE '%специалист по информационной безопасности%')
                OR (LOWER(vacancy) LIKE '%безопасность%')
                OR (LOWER(vacancy) LIKE '%защита%')
                OR (LOWER(vacancy) LIKE '%information security specialist%')
                OR (LOWER(vacancy) LIKE '%information security%')
                OR (LOWER(vacancy) LIKE '%фахівець служби безпеки%')
                OR (LOWER(vacancy) LIKE '%cyber security%')) and year == '{year}'
        group by skill),
        Sum as (select sum(count) as total from Top)
        select year, skill, count, round(CAST(count as REAL) / total,4) * 100 as ratio from Top,Sum
        order by count
        desc limit 10""")])
convertedVacanciesDB.CloseDB()

report = Report("Специалист по информационной безопасности")

statisticsByYear = pd.merge(pd.merge(avgSalary, avgSalaryByVacancy, on='publishedYear'),
                            pd.merge(countVacancies, countVacancy, on='publishedYear'),
                            on='publishedYear')
# report.GenerateImages(statisticsByYear.to_dict(), avgCitySalary.set_index('salaryAreaName').to_dict(),
#                       avgCityCount.set_index('countAreaName').to_dict())

InsertData(models.StatisticsByYear, statisticsByYear.reset_index())
InsertData(models.SalaryStatisticsByArea, avgCitySalary)
InsertData(models.RatioStatisticsByArea, avgCityCount)
InsertData(models.SkillsStatisticsByYear, skillsStatistics)
