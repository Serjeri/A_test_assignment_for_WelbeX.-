from django.db import models
# Работа с БД и таблицей

# Создание таблицы id по умолчанию

#Таблица должна иметь сортировку по всем полям кроме даты. Фильтрация должна быть в виде двух выпадающих списков и текстового поля:
#Выбор колонки, по которой будет фильтрация
#Выбор условия (равно, содержит, больше, меньше)
#Поле для ввода значения для фильтрации

class tableValuem(models.Model):
    data = models.DateField('Data')
    title = models.CharField('title', max_length=250)
    quantity = models.IntegerField('quantity')
    distance = models.IntegerField('distance')

    def __set__(self):
        return self.data
    