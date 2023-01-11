from vacanciesAnalysisApp.services import responses

def InitializeDB():
    from vacanciesParser import VacanciesParser
    fileName = input("Введите название файла: ")
    currenciesParser = VacanciesParser(fileName)
    convertedVacanciesDB, convertedVacanciesDF = currenciesParser.ConvertToRub()
    CreateSkillsTable(convertedVacanciesDB, convertedVacanciesDF)
    return convertedVacanciesDB


def CreateSkillsTable(db, df):
    import pandas as pd
    df = df[df["key_skills"].notnull()]
    vacanciesName = []
    skills = []
    years = []
    for skillsByVacancy, vacancy, year in zip(df['key_skills'], df['name'], df['published_at']):
        tmp = skillsByVacancy.split('\n')
        vacanciesName.extend([vacancy] * len(tmp))
        years.extend([year[:4]] * len(tmp))
        skills.extend(tmp)
    db.tableName = 'Skills'
    db.CreateTableDataBase(pd.DataFrame({'vacancy': vacanciesName, 'skill': skills, 'year': years}),
                           'vacancy text, skill text, year text', False)
