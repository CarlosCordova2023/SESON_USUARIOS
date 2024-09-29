from django.contrib import admin
from .models import Book

#@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author','valoracion', 'published_date', 'rating', 'fecha_creacion', 'fecha_modificacion')
    search_fields = ('title', 'author')
    readonly_fields = ('fecha_creacion', 'fecha_modificacion')
    list_filter = ('valoracion', 'fecha_modificacion')

admin.site.register(Book, BookAdmin)
