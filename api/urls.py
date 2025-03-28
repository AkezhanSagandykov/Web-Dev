from django.urls import path
from .views import CompanyListView, CompanyDetailView, VacancyListView, VacancyDetailView, VacanciesByCompanyView, Top10VacanciesByDecreasingSalaryView
urlpatterns = [
    path('companies/', CompanyListView.as_view(), name='company-list'),
    path('companies/<int:pk>/', CompanyDetailView.as_view(), name='comapany-detail'),
    path('companies/<int:company_id>/vacancies/', VacanciesByCompanyView.as_view(), name='vacancies-by-company'),
    path('vacancies/', VacancyListView.as_view(), name='vacancy-list'),
    path('vacancies/<int:pk>/', VacancyDetailView.as_view(), name='vacancy-detail'),
    path('vacancies/top_ten/', Top10VacanciesByDecreasingSalaryView.as_view(), name='vacancy-top-ten')
]
