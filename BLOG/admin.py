from django.contrib import admin
from .models import BLOG
from django.contrib.auth.models import Group


class BlogAdnim(admin.ModelAdmin):
    pass


admin.site.register(BLOG, BlogAdnim)
admin.site.unregister(Group)
