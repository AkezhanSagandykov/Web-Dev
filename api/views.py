from django.shortcuts import render
from rest_framework import generics
from .models import Company, Vacancy
from .serializers import CompanySerializer, VacancySerializer
class CompanyListView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
class CompanyDetailView(generics.RetrieveAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
class VacancyListView(generics.ListAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
class VacancyDetailView(generics.RetrieveAPIView):
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
class VacanciesByCompanyView(generics.ListAPIView):
    serializer_class = VacancySerializer
    def get_queryset(self):
        company_id = self.kwargs['company_id']
        return Vacancy.objects.filter(compmay__id=company_id)
class Top10VacanciesByDecreasingSalaryView(generics.ListAPIView):
    serializer_class = VacancySerializer
    def get_queryset(self):
        return Vacancy.objects.order_by('-salary'[:10])