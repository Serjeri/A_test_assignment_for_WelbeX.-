from .models import tableValuem
from .Form import valueFilterUI,sortingValium

class Filtering_logic:
    def __init__(self,valueUI:valueFilterUI, sorting:sortingValium):
        self.valueUI = valueUI
        self.sorting = sorting
        
    def getResult(self):
        table = tableValuem.objects.all()#вызов базы из модели,передача как ключ значение
        #логика фильтрации и сортировки
        if self.valueUI.is_valid():
            fields_name = self.valueUI.cleaned_data["fields_name"]
            expressions = self.valueUI.cleaned_data["expressions"]
            value = self.valueUI.cleaned_data["value"]
            
            match fields_name:
                case 'title':
                    if expressions == 'contains':
                        table=table.filter(title__contains = value)
                case 'quantity':
                    match expressions:
                        case 'gt':
                            table=table.filter(quantity__gt = value)
                        case 'lt':
                            table=table.filter(quantity__lt = value)
                        case 'equal':
                            table=table.filter(quantity = value)
                case 'distance':
                        match expressions:
                            case 'gt':
                                table=table.filter(distance__gt = value)
                            case 'lt':
                                table=table.filter(distance__lt = value)
                            case 'equal':
                                table=table.filter(distance = value)
        if self.sorting.is_valid():
            sorting = self.sorting.cleaned_data["sorting"]
            if sorting:
                table = table.order_by(sorting)
            if sorting == ' ':
                table = table.order_by(sorting)
        return table
    