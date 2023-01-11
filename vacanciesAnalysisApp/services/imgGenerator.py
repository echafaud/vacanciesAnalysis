import numpy as np
import matplotlib.pyplot as plt
from matplotlib.transforms import Bbox

class Report:
    """
    Класс, формирующий отчет для пользователя
    """

    def __init__(self, vacancyName):
        """
        Инициализирует объект Report

        Args:
            vacancyName (str): название профессии
        """

        self.vacancyName = vacancyName

    def CheckEmptyText(self, value):
        """
        Проверяет ячейку на пустоту,
        если ячейка пустая (None) - задает ячейке значение ""

        Args:
            value (str): Ячейка таблицы

        Returns:
            str: значение ячейки
        """
        if value is None:
            return ""
        return str(value)

    def __CreateVerticalBars(self, ax, title, data1, data2, label1, label2, rotation):
        """
        Формирует вертикальную диаграмму для двух данных

        Args:
            ax (axes.SubplotBase): График
            title (str): Заголовок диаграммы
            data1 (dict): Общие данные
            data2 (dict): Данные для выбранной профессии
            label1 (str): Надпись легенды для общих данных
            label2 (str): Надпись легенды для данные выбранной профессии
            rotation (int): Угол поворота надписей оси X

        Returns:
            axes.SubplotBase: График
        """
        xIndexes = np.arange(len(data1.keys()))
        width = 0.35
        ax.set_title(title)
        ax.bar(xIndexes - width / 2, data1.values(), width, label=label1)
        ax.bar(xIndexes + width / 2, data2.values(), width, label=label2)
        ax.legend()
        ax.grid(axis="y", visible=True)
        ax.set_xticks(xIndexes, data1.keys(), rotation=rotation)
        return ax

    def __CreateHorizontalBar(self, ax, title, data):
        """
        Формирует горизонтальную диаграмму

        Args:
            ax (axes.SubplotBase): График
            title (str): Заголовок диаграммы
            data (dict): Данные

        Returns:
            axes.SubplotBase: График
        """
        width = 0.35
        ax.set_title(title)
        ax.barh(list(data.keys())[:10], list(data.values())[:10], width)
        ax.grid(axis="x", visible=True)
        ax.invert_yaxis()
        return ax

    def __CreatePie(self, ax, title, data):
        """
        Формирует круговую диаграмму
        Args:
            ax (axes.SubplotBase): График
            title (str): Заголовок диаграммы
            data (dict): Данные

        Returns:
            axes.SubplotBase: График
        """
        plt.rc('font', size=6)
        ax.set_title(title)
        ax.pie(data.values(), labels=data.keys(), labeldistance=1.1, startangle=-210)
        return ax

    def GenerateImages(self, dataByYear, salaryDataByArea,countDataByArea):
        """
        Формирует изображения со статистикой вакансий в виде графиков

        Args:
            data: Данные файла
        """
        plt.rc('font', size=8)
        figure = plt.figure()
        ax = figure.add_subplot()
        ax = self.__CreateVerticalBars(ax, f"Уровень зарплат по годам", dataByYear['avgSalary'],
                                        dataByYear['avgSalaryByVacancy'],
                                        "средняя з/п",
                                        f'з/п {self.vacancyName}', 90)
        figure.savefig(f'{ax.get_title()}')
        figure.clear()
        ax = figure.add_subplot()
        ax = self.__CreateVerticalBars(ax, f"Количество вакансий по годам", dataByYear['countVacancies'],
                                        dataByYear['countVacancy'],
                                        "Количество вакансий", f'Количество вакансий {self.vacancyName}', 90)
        figure.savefig(f'{ax.get_title()}')
        figure.clear()
        ax = figure.add_subplot()
        ax = self.__CreateHorizontalBar(ax, "Уровень зарплат по городам", salaryDataByArea['avgSalaryByArea'])
        figure.savefig(f'{ax.get_title()}')
        figure.clear()
        ax = figure.add_subplot()
        plt.rc('font', size=6)
        tempDict = {k: v for k, v in countDataByArea['ratioByArea'].items()}
        tempDict["Другие"] = 1 - sum(tempDict.values())
        tempDict = dict(sorted(tempDict.items(), key=lambda x: x[1]))
        ax = self.__CreatePie(ax, "Доля вакансий по городам", tempDict)
        plt.tight_layout()
        figure.savefig(f'{ax.get_title()}')

    #     plt.rc('font', size=8)
    #     figure = plt.figure()
    #     ax1 = figure.add_subplot(2, 2, 1)
    #     ax2 = figure.add_subplot(2, 2, 2)
    #     ax1 = self.__CreateVerticalBars(ax1, f"Уровень зарплат по годам", dataByYear['avgSalary'],
    #                                     dataByYear['avgSalaryByVacancy'],
    #                                     "средняя з/п",
    #                                     f'з/п {self.vacancyName}', 90)
    #
    #     ax2 = self.__CreateVerticalBars(ax2, f"Количество вакансий по годам", dataByYear['countVacancies'],
    #                                     dataByYear['countVacancy'],
    #                                     "Количество вакансий", f'Количество вакансий {self.vacancyName}', 90)
    #     ax3 = figure.add_subplot(2, 2, 3)
    #     ax3 = self.__CreateHorizontalBar(ax3, "Уровень зарплат по городам", salaryDataByArea['avgSalaryByArea'])
    #     plt.rc('font', size=6)
    #     tempDict = {k: v for k, v in countDataByArea['ratioByArea'].items()}
    #     tempDict["Другие"] = 1 - sum(tempDict.values())
    #     tempDict = dict(sorted(tempDict.items(), key=lambda x: x[1]))
    #     ax4 = figure.add_subplot(2, 2, 4)
    #     ax4 = self.__CreatePie(ax4, "Доля вакансий по городам", tempDict)
    #     plt.tight_layout()
    #
    #     for ax in figure.axes:
    #         self.SaveSubplot(figure, ax)
    #
    # def SaveSubplot(self, figure, ax):
    #     extent = self.full_extent(ax).transformed(figure.dpi_scale_trans.inverted())
    #     figure.savefig(f'{ax.get_title()}', bbox_inches=extent)
    #
    # def full_extent(self, ax, pad=0.0):
    #     """Get the full extent of an axes, including axes labels, tick labels, and
    #     titles."""
    #     # For text objects, we need to draw the figure first, otherwise the extents
    #     # are undefined.
    #     ax.figure.canvas.draw()
    #     items = ax.get_xticklabels() + ax.get_yticklabels()
    #     #    items += [ax, ax.title, ax.xaxis.label, ax.yaxis.label]
    #     items += [ax, ax.title]
    #     bbox = Bbox.union([item.get_window_extent() for item in items])
    #
    #     return bbox.expanded(1.0 + pad, 1.0 + pad)
