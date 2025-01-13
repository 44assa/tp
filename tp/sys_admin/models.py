from django.db import models


class MainPageContent(models.Model):
    description = models.TextField(blank=True, verbose_name='Описание профессии')
    image = models.ImageField(upload_to='uploads/main_page/%Y/%m/%d', verbose_name='Фото')


class DemandData(models.Model):
    salary_chart = models.ImageField(upload_to='uploads/demand/%Y/%m/%d', verbose_name='График зарплат по годам')
    vacancy_chart = models.ImageField(upload_to='uploads/demand/%Y/%m/%d', verbose_name='График вакансий по годам')
    demand_table = models.TextField(verbose_name='Таблица востребованности')


class GeographyData(models.Model):
    city_salary_chart = models.ImageField(upload_to='uploads/geography/%Y/%m/%d', verbose_name='График зарплат по городам')
    city_vacancy_chart = models.ImageField(upload_to='uploads/geography/%Y/%m/%d', verbose_name='График вакансий по городам')
    geography_table = models.TextField(verbose_name='Таблица географии')


class SkillsetData(models.Model):
    table_title = models.CharField(max_length=50, verbose_name='Название таблицы')
    skills_table = models.TextField(verbose_name='Таблица навыков')
    skills_chart = models.ImageField(upload_to='uploads/skills/%Y/%m/%d', verbose_name='График навыков')


class RecentVacancy(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название')
    vacancy_query = models.TextField(verbose_name='Запрос для поиска вакансий')
