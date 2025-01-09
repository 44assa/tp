from django.db import models

class LandingPageContent(models.Model):
    description = models.TextField(blank=True, verbose_name='Описание основной информации')
    image = models.ImageField(upload_to='uploads/images/%Y/%m/%d', blank=False, verbose_name='Изображение')

class MarketTrends(models.Model):
    salary_trend_chart = models.ImageField(upload_to='uploads/images/%Y/%m/%d', blank=False, verbose_name='Диаграмма изменения зарплат')
    vacancy_trend_chart = models.ImageField(upload_to='uploads/images/%Y/%m/%d', blank=False, verbose_name='Диаграмма изменения вакансий')
    trend_table = models.TextField(blank=False, verbose_name='Сводная таблица тенденций')

class RegionalStatistics(models.Model):
    city_salary_chart = models.ImageField(upload_to='uploads/images/%Y/%m/%d', blank=False, verbose_name='Диаграмма зарплат по регионам')
    city_vacancy_share_chart = models.ImageField(upload_to='uploads/images/%Y/%m/%d', blank=False, verbose_name='Диаграмма доли вакансий по регионам')
    regional_table = models.TextField(blank=False, verbose_name='Таблица региональной статистики')

class CompetencyAnalytics(models.Model):
    table_title = models.TextField(blank=False, verbose_name='Заголовок таблицы', max_length=30)
    competency_table = models.TextField(blank=False, verbose_name='Таблица компетенций')
    skills_chart = models.ImageField(upload_to='uploads/images/%Y/%m/%d', blank=False, verbose_name='Диаграмма ключевых навыков')

class RecentJobListing(models.Model):
    headline = models.CharField(max_length=100, verbose_name='Название вакансии')
    target_vacancy = models.TextField(blank=False, verbose_name='Целевая вакансия для анализа')
