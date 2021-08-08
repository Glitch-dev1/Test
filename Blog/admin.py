from django.contrib import admin

from .models import Article

admin.site.site_header = 'Test Admin'
admin.site.index_title = 'Admin panel'

admin.site.register(Article)
