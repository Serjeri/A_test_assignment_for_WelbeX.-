from django.db import models
# Работа с БД и таблицей

# Создание таблицы id по умолчанию

class tableValuem(models.Model):
    data = models.DateField('Data')
    title = models.CharField('title', max_length=250)
    quantity = models.IntegerField('quantity')
    distance = models.IntegerField('distance')

    def __set__(self):
        return self.data
    