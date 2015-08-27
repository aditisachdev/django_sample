from django.contrib import admin

# Register your models here.

from .models import *

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'publisher', 'genre', 'edition')
	list_filter = ['pub_date','author']
	search_fields = ['title','genre']

admin.site.register(Book,BookAdmin)
admin.site.register(Review)

#class ReviewAdmin(admin.ModelAdmin):
