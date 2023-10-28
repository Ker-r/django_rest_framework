from django.contrib import admin
from .models import Animal, Category


# Register your models here.
class AnimalAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'title', )
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('title',)
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка
    empty_value_display = '-пусто-'


class CategoryAdmin(admin.ModelAdmin):
    # Перечисляем поля, которые должны отображаться в админке
    list_display = ('pk', 'name', )
    # Добавляем интерфейс для поиска по тексту постов
    search_fields = ('name',)
    # Это свойство сработает для всех колонок: где пусто — там будет эта строка
    empty_value_display = '-пусто-'


# При регистрации модели Staff источником конфигурации для неё назначаем
# класс StaffAdmin
admin.site.register(Animal, AnimalAdmin)
admin.site.register(Category, CategoryAdmin)
