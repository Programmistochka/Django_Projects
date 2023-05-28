from django.db import models


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    name = models.CharField(max_length=250, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=300, null=False)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=200) # noqa Если не указывать входной параметр db_column для поля SlugField, то автоматически будет использовать значение из поля name

    def __str__(self):
        return self.name
