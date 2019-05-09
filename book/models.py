from django.db import models


class Book(models.Model):
    name = models.CharField(max_length=200)
    pages = models.IntegerField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('book_edit', kwargs={'pk': self.pk})
