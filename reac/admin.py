from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(ata)
class ata_Admin(admin.ModelAdmin):
    list_display = ('chapter', 'section', 'subject', 'title', 'zh_title',)
    list_filter = ('zh_title',)
    search_fields = ('chapter', 'section', 'subject', 'title', 'zh_title',)

@admin.register(fm)
class fm_Admin(admin.ModelAdmin):
    list_display = ('fm', 'ata', 'fe', 'ru', 're',)
    list_filter = ('fm',)
    search_fields = ('fm', 'fe', 'ru', 're',)

@admin.register(ac)
class ac_Aminn(admin.ModelAdmin):
    list_display = ('tail_number', 'acmodels',)
    list_filter = ('tail_number',)
    search_fields = ('tail_number', 'acmodels',)

@admin.register(acmodels)
class acmodels_Aminn(admin.ModelAdmin):
    list_display = ('basic_acmodels', 'expanded_acmodels', 'if_intra_ac', )
    list_filter = ('basic_acmodels',)
    search_fields = ('basic_acmodels',)
