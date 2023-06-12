from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Tag, Scope

class ScopeInlineFormset(BaseInlineFormSet):
        
    def clean(self):
        count = 0 # Счетчик основных тегов
        for form in self.forms:
            # В form.cleaned_data должен быть словарь с данными каждой отдельной формы
            # данные можно проверить
            if form.cleaned_data.get('is_main') == True:
                count += 1 

        if count == 0:
            raise ValidationError(f'Ошибка: не указан основной раздел')
        elif count > 1:
            raise ValidationError(f'Ошибка: может быть только один основной раздел')
        return super().clean() # вызов базового кода переопределяемого метода


class ScopesInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset 

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'text', 'published_at', 'image']
    inlines = [ScopesInline]

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
