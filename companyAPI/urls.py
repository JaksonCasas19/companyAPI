from companyAPI.views import CompanyListView
from django.urls import path


urlpatterns = [
    path('company/', CompanyListView, name='company_list'),
]
