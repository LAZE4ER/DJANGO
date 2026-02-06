from django.contrib import admin
from .models import Author, Book

# 2. Книги всередині автора (Inline)
class BookInline(admin.TabularInline): 
    model = Book
    extra = 1 
    max_num = 10 


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'birth_date', 'books_count') 
    search_fields = ('name', 'surname') 
    inlines = [BookInline] 

    def books_count(self, obj):
        return obj.books.count()
    books_count.short_description = "Кількість книг"


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
   
    list_display = ('title', 'author', 'status', 'is_classic') 
    list_filter = ('status', 'published_year') 
    search_fields = ('title', 'isbn') 
    list_editable = ('status',) 

    
    def is_classic(self, obj): 
        return obj.published_year < 1950
    is_classic.boolean = True 
    is_classic.short_description = "Класика?"

   
    fieldsets = (
        ("Основна інформація", {
            'fields': ('title', 'author', 'isbn')
        }),
        ("Метадані та статус", {
            'fields': ('status', 'published_year', 'created_at'),
            'classes': ('collapse',), 
        }),
    )

    
    readonly_fields = ('created_at',) 

   
    actions = ['make_rented', 'make_available']

@admin.action(description="Позначити обрані книги як 'Видані'")
    def make_rented(self, request, queryset):
        updated = queryset.update(status='rented')
        self.message_user(request, f"Статус змінено для {updated} книг.")

@admin.action(description="Позначити обрані книги як 'В наявності'")
    def make_available(self, request, queryset):
        updated = queryset.update(status='available')
        self.message_user(request, f"{updated} книг тепер знову в бібліотеці.")




