from django.shortcuts import render
from django.http import Http404, HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }

def main_view(request):
    dishes = (', ').join(DATA.keys())
    return HttpResponse(f'Для получения рецепта необходимо в строке адреса указать наименование блюд и количество порций.\n Варианты {dishes}. Можно указать количество порций через знак "?". Например: http://127.0.0.1:8000/omlet?servings=2 ')

def view_ingrids(request, dish):
    if dish in DATA.keys():
        portions = int(request.GET.get("servings", 1))
        #print(portions)
        context = {
            'recipe': DATA.get(dish)
            }
        for ingr, amount in context['recipe'].items():
                amount*=portions
                context['recipe'][ingr]=round(amount, 2)  
    else:
        raise Http404
    return render(request, 'calculator/index.html', context)
