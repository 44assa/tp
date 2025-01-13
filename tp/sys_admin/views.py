import re

import requests
from django.shortcuts import render
from .models import *
from .hh import ApiHeadHunter

def fetch_vacancies(request):
    vacancies = RecentVacancy.objects.all()
    if vacancies.exists():
        query = vacancies.last().vacancy_query
        headhunter = ApiHeadHunter(query)
        vacancy_data = headhunter.fetch_vacancies('2025-01-11', 10)
        context = {'vacancy_data': vacancy_data, 'vacancies': vacancies}
        return render(request, 'vacancies.html', context)
    return render(request, 'vacancies.html', {'vacancy_data': [], 'vacancies': vacancies})


def main_page(request):
    content = MainPageContent.objects.all()
    return render(request, 'main_page.html', {'content': content})


def demand_page(request):
    demand_info = DemandData.objects.all()
    return render(request, 'demand_page.html', {'demand_info': demand_info})


def geography_page(request):
    geography_info = GeographyData.objects.all()
    return render(request, 'geography_page.html', {'geography_info': geography_info})


def skills_page(request):
    skills_info = SkillsetData.objects.all()
    return render(request, 'skills_page.html', {'skills_info': skills_info})


def general_page(request):
    return render(request, 'general.html')