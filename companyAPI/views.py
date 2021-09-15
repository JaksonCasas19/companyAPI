from django.shortcuts import render
from django.views import View
from .models import Company
from django.http import JsonResponse
from django.forms.models import model_to_dict

# Create your views here.
#Clase para devolver toda la lista
class CompanyListView(View):
    def get(self,request):
        #get
        xlist = Company.objects.all()
        return JsonResponse(list(xlist.values()),safe=False) #Va devolver un array de objetos Json

#Clase para devolver un registro
class CompanyDetailView(View):
    def get(self,request,pk):
        #get
        company = Company.objects.get(pk=pk)
        return JsonResponse(model_to_dict(company)) #Va devolver un diccionario