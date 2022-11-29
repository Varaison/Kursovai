from django.contrib import admin
from .models import *


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo', 'price', 'cat')
    list_display_links = ('id',)
    search_fields = ('name', 'content')
    list_editable = ('name', 'price')
    list_filter = ('id', 'name', 'price', 'cat')
    prepopulated_fields = {'slug': ('name',)}

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


# admin.site.register(Musicant)
# admin.site.register(Users)
admin.site.register(Service, ServiceAdmin)
# admin.site.register(Producer)
# admin.site.register(Support)
# admin.site.register(Offer)
admin.site.register(Category, CategoryAdmin)