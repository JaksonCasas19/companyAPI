from django.shortcuts import render
from django.views import View
from .models import Company
from django.http import JsonResponse

# Create your views here.
class CompanyView(View):
    def get(self,request):
        #ger
        list = Company.objects.all()
        return JsonResponse(list,False) #Va devolver un array de objetos Json

    def post(self,request):
        #post
    def put(self,request):
        #put
    def delete(self,request):
        #delete