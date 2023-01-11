import re
import requests
import pandas as pd


class DistributorVacancies:

    def GetResponse(self, url):
        for i in range(1000):
            response = requests.get(url)
            if response.ok:
                print("OK")
                return response
        raise requests.exceptions.ConnectionError("Сервер не отвечает")

    # def GetVacancies(self, timeRange):
    #     firstDate, endDate = timeRange
    #     firstDate, endDate = firstDate.strftime("%Y-%m-%dT%X"), endDate.strftime("%Y-%m-%dT%X")
    #     generalURL = f'https://api.hh.ru/vacancies?date_from={firstDate}&date_to={endDate}&specialization=1&per_page=100'
    #     generalResponse = self.GetResponse(generalURL)
    #     jsonFile = generalResponse.json()
    #     pages = jsonFile['pages']
    #     vacancies = []
    #     for page in range(pages):
    #         pageURL = f'https://api.hh.ru/vacancies?date_from={firstDate}&date_to={endDate}&specialization=1&per_page=100&page={page}'
    #         vacancies += self.GetVacanciesByPage(pageURL)
    #     print(len(vacancies))
    #     return vacancies

    def CleanRow(self, row):
        cleaner = re.compile('<.*?>')
        clearedRow = re.sub(cleaner, '', row)
        return clearedRow

    def GetAvgSalary(self, salaryFrom, salaryTo):
        salaryFrom = float(salaryFrom or 0)
        salaryTo = float(salaryTo or 0)
        return (salaryFrom + salaryTo) / 2

    def GetVacanciesByPage(self, url):
        vacanciesByPage = []
        pageResponse = self.GetResponse(url)
        pageJson = pageResponse.json()
        for vacancy in pageJson['items']:
            id = vacancy['id']
            vacancy = self.GetResponse(f'https://api.hh.ru/vacancies/{id}').json()
            salaryExist = vacancy['salary']
            tempVacancy = {'name': vacancy['name'],
                           'description': self.CleanRow(vacancy['description'])[:100],
                           'skills': vacancy['key_skills'],
                           'employer': vacancy['employer']['name'],
                           'salary': self.GetAvgSalary(vacancy['salary']['from'],
                                                       vacancy['salary']['to']) if salaryExist else None,
                           'salary_currency': vacancy['salary']['currency'] if salaryExist else None,
                           'area_name': vacancy['area']['name'],
                           'published_at': vacancy['published_at']}
            vacanciesByPage.append(tempVacancy)
        return vacanciesByPage

    # def GetVacanciesCSV(self, date, deltaTimeRange):
    #     df = pd.DataFrame()
    #     date = date.normalize()
    #     multiplyHour = int(24 / deltaTimeRange)
    #     for i in range(deltaTimeRange):
    #         timeRange = self.GetTimeRange(date, multiplyHour)
    #         date = timeRange[1]
    #          df = pd.concat([df, pd.DataFrame(self.GetVacancies(timeRange))])
    #
    #     df.to_csv("DistributorVacancies.csv", index=False)

    # def GetTimeRange(self, date, multiplyHour):
    #     return pd.date_range(date, periods=2, freq=f'{multiplyHour}H')

    def GetRecentVacancies(self, date):
        request = f'https://api.hh.ru/vacancies?text=безопасность+OR+защита+OR+"information security specialist"+OR+' \
                  f'"information security"+OR+"фахівець служби безпеки"+OR+"cyber security"&search_field=name' \
                  f'&order_by=publication_time&date_from={date}&date_to={date}&specialization=1&per_page=10'
        recentVacancies = self.GetVacanciesByPage(request)
        return recentVacancies
