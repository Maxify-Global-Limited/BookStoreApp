from django.contrib import admin

from .models import Book, Review, Genre, Author


class ReviewInline(admin.TabularInline):
    model = Review
    
class BookAdmin(admin.ModelAdmin):
    inlines = [ ReviewInline, ]
    list_display = ("title", "author", "price",)
    
    
admin.site.register(Book, BookAdmin)
admin.site.register(Genre)
admin.site.register(Author)