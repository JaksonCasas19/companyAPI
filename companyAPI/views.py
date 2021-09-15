from django.shortcuts import render
from django.views import View
from .models import Company
from django.http import JsonResponse

# Create your views here.
#Clase para devolver toda la lista
class CompanyListView(View):
    def get(self,request):
        #ger
        list = Company.objects.all()
        return JsonResponse(list,False) #Va devolver un array de objetos Json

#Clase para devolver un registro
class CompanyDetailView(View):
    def get(self,request,pk):
        #ger
        list = Company.objects.get(pk=pk)
        return JsonResponse(list,False) #Va devolver un array de objetos Json