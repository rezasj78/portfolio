from django.contrib import admin
from .models import job

admin.site.site_header = 'ADMIN'


class jobAdmin(admin.ModelAdmin):
    list_display = ['summery']
    list_filter = ['summery']


admin.site.register(job, jobAdmin)
