from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ім'я")
    surname = models.CharField(max_length=100, verbose_name="Прізвище")
    birth_date = models.DateField(verbose_name="Дата народження", null=True, blank=True)

    def __str__(self):
        return f"{self.name} {self.surname}"

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Автори"

class Book(models.Model):
    STATUS_CHOICES = [
        ('available', 'В наявності'),
        ('rented', 'Видана'),
    ]

    title = models.CharField(max_length=200, verbose_name="Назва")
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books', verbose_name="Автор")
    published_year = models.PositiveIntegerField(verbose_name="Рік видання")
    isbn = models.CharField(max_length=13, verbose_name="ISBN", unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available', verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Додано в базу")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"