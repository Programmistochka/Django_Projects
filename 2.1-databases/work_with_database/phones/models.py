from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=250 nul=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField
    release_date = models.DateField
    lte_exist = models.BooleanField
    slug = models.SlugField(max_length=200) #Если не указывать входной параметр db_column для поля SlugField, то автоматически будет использовать значение из поля name