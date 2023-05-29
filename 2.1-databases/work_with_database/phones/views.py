from django.shortcuts import render, redirect
from .models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_inf = Phone.objects.all()   

    # Сортировка объектов из БД по полям name и price
    # Вид сортировки в функцию передается из Get-параметра 'sort'
    sort_type = request.GET.get('sort')
    if sort_type == 'name':
        phones_inf = phones_inf.order_by('name')
    elif sort_type == 'min_price':
        phones_inf = phones_inf.order_by('price')
    elif sort_type == 'max_price':
        phones_inf = phones_inf.order_by('-price')    
    context = {'phones': phones_inf}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {'phone': phone}
    return render(request, template, context)
