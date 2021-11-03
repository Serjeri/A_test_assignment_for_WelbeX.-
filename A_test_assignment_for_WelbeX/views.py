from django import forms
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db import models
from django.shortcuts import render
from .models import tableValuem
from django.http import JsonResponse
from django.core import serializers
from django_filters.filters import NumberFilter
import django_filters
from .Form import filterValium



def index(request):
   #b = tableValuem(data = '1988-12-05', title = 't', distance = 3, quantity = 56)
   #b.save()
   table = tableValuem.objects.all()       # передача как ключ значение
   form = filterValium(request.GET)
   pageNumber = request.GET.get('pageNumber', 1)
   if form.is_valid():
      #if form.cleaned_data["title"]:
      #   table = table.filter(title=form.cleaned_data["title"])
      #   
      #if form.cleaned_data["quantity"]:
      #   table = table.filter(quantity__gte=form.cleaned_data["quantity"])
      #   
      #if form.cleaned_data["distance"]:
      #   table = table.filter(quantity__lte=form.cleaned_data["distance"])
         
      #if form.cleaned_data["ordering"]:
      #   table = table.order_by(form.cleaned_data["ordering"])
         
      if form.cleaned_data["filters"]:
         table = table.order_by(form.cleaned_data["filters"])
         
   paginator = Paginator(table, 3)
   page_obj = paginator.get_page(pageNumber)
   try:
      table = paginator.page(page_obj)
   except PageNotAnInteger:
      table = paginator.page(1)
   except EmptyPage:
      table = paginator.page(paginator.num_pages)
   return render(request, 'index.html', {'table': page_obj , "form":form})

def httpResponse(request):
   pageNumber = request.GET.get('pageNumber', 1)
   table = tableValuem.objects.all()        # передача как ключ значение
   paginator = Paginator(table, 3) # подготовка пагинатора
   page_obj = paginator.get_page(pageNumber)
   pythonserializer = serializers.get_serializer("python")()
   serializedpage = pythonserializer.serialize(page_obj.object_list, 
            fields=('data', 'title','quantity','distance')) 
   return JsonResponse(serializedpage, safe=False)
