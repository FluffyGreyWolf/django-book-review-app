from django.contrib import admin
from reviews.models import Publisher, Contributor, Book, BookContributor, Review

class BookAdmin(admin.ModelAdmin):
    model = Book
    list_display = ('title', 'isbn', 'get_publisher', 'publication_date')
    search_fields = ['title', 'publisher__name']

    def get_publisher(self, obj):
        return obj.publisher.name

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Contributor)
admin.site.register(Book, BookAdmin)
admin.site.register(BookContributor)
admin.site.register(Review)