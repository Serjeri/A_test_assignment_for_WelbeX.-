from django import forms


class Table(forms.Form):
    ordering = forms.ChoiceField(label="сортировка", required=False, choices=[
        ["name", "по алфовиту"],
        ["price", "def"],
         ])
    
    
class filterValium(forms.Form):
    #title = forms.CharField(label="Название",required=False)
    #quantity = forms.IntegerField(label="Количество",required=False)
    #distance = forms.IntegerField(label="Расстоняние",required=False)
    filters = forms.ChoiceField(label='Фильтрация', required=False, choices=[
        ['title','Название'],['quantity','Количество'],['distance','Расстояние']
    ])
    #ordering = forms.ChoiceField(label='Сортировка', required=False, choices=[
    #    ['quantity','Больше'],['-quantity','Меньше'],['=', 'Равно']
    #])