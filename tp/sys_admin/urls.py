from django.urls import path

from .views import *

urlpatterns = [
    path('', main_page, name='home'),
    path('all/', general_page, name='all'),
    path('demend/', demand_page, name='demend'),
    path('geography/', geography_page, name='geography'),
    path('skills/', skills_page, name='skills'),
    path('lastVacancy/', fetch_vacancies, name='lastVacancy'),
]