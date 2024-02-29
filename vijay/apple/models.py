from django.db import models
from django.contrib import admin
class Book(models.Model):
     BookId=models.IntegerField(primary_key=True);
     BookName=models.CharField(max_length=20);
     BookAuthor=models.CharField(max_length=20);
     BookPrice=models.IntegerField();
     BookGenre=models.CharField(max_length=20);
class BookAdmin(admin.ModelAdmin):
     list_display=('BookId','BookName','BookAuthor','BookPrice','BookGenre');