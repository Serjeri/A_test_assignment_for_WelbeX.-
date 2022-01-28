from django import forms


class Table(forms.Form):
    ordering = forms.ChoiceField(label="сортировка", required=False, choices=[
        ["name", "по алфовиту"],
        ["price", "def"],
         ])
    
class sortingValium(forms.Form):
    
    sorting = forms.ChoiceField(label='Сортировка', required=False, choices=[
        [ 'id',' '],["title",'Название'],['quantity','Количество'],['distance','Расстояние']])
    
    
class valueFilterUI(forms.Form):

    fields_name = forms.ChoiceField(label='Выбор колонки', required=False, choices=[
       ["title",'Название'],['quantity','Количество'],['distance','Расстояние']])

    expressions = forms.ChoiceField(label='Выбор выражения', required=False, choices=[
       ['gt','>'],['lt','<'],['equal','='],['contains','содержит']])

    value = forms.CharField(label='Введите значение', required=False)
