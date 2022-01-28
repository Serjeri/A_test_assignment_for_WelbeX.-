from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .Form import sortingValium, valueFilterUI
from .business_logic import Filtering_logic



def index(client):
   sorting = sortingValium(client.GET)#Берется значение из сортировки во Form
   valueUI = valueFilterUI(client.GET)#Фильтрация сделланая во Form 
   logic = Filtering_logic(valueUI, sorting)#Бизнес логика
   result = logic.getResult()#Вызывает метод в бизнес логике
   pageNumber = client.GET.get('pageNumber', 1)#перенести в бизнес логику
   paginator = Paginator(result, 3)#перенести в бизнес логику
   page_obj = paginator.get_page(pageNumber)#перенести в бизнес логику
   return render(client, 'index.html', {'table': page_obj , "sorting":sorting, "valueUI":valueUI})#отрисовка на клиенте

def httpResponse(client):
   sorting = sortingValium(client.GET)
   valueUI = valueFilterUI(client.GET)
   logic = Filtering_logic(valueUI,sorting)
   result = logic.getResult() #client.GET то что пришло с клиента
   pageNumber = client.GET.get('pageNumber', 1)
   paginator = Paginator(result, 3) # подготовка пагинатора
   page_obj = paginator.get_page(pageNumber)
   pythonserializer = serializers.get_serializer("python")()
   serializedpage = pythonserializer.serialize(page_obj.object_list, 
            fields=('data', 'title','quantity','distance')) 
   return JsonResponse(serializedpage, safe=False)
