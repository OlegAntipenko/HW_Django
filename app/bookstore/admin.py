from django.contrib import admin
from .models import Books, Authors, Comments

admin.site.register(Authors)
admin.site.register(Books)
admin.site.register(Comments)
