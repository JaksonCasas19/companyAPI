from companyAPI.views import CompanyListView,CompanyDetailView
from django.urls import path


urlpatterns = [
    path('company/', CompanyListView.as_view(), name='company_list'),
    path('company/<int:pk>', CompanyDetailView.as_view(), name='company'),
]
