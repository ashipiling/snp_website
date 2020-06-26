# Register your models here.
from django.contrib import admin
from .models import SNP


class SNPAdmin(admin.ModelAdmin):
    list_display = ['snp_type', 'location', 'isolated_time', 'created_time', 'modified_time', 'author']

admin.site.register(SNP, SNPAdmin)