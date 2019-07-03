from django.contrib import admin
from .models import terms
from .models import acronyms
from .models import term_category
from .models import acr_category

# Register your models here.
@admin.register(terms)
class terms_Admin(admin.ModelAdmin):
    list_display = ('title', 'content', 'category', 'acmodels', 'tags', 'source')
    list_filter = ('title',)
    search_fields = ('title','category',)

@admin.register(acronyms)
class acronyms_Admin(admin.ModelAdmin):
    list_display = ('name', 'category', 'full_name', 'zh_name', 'tags')
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(term_category)
class term_category_Admin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    list_filter = ('name',)
    search_fields = ('name',)

@admin.register(acr_category)
class acr_category_Admin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    list_filter = ('name',)
    search_fields = ('name',)
# Register your models here.
