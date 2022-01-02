from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')
    text = models.TextField(verbose_name='Text')
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, verbose_name='Категория')
    author = models.ForeignKey(to='Author', on_delete=models.CASCADE, verbose_name='Автор', null=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name='Name')
    surname = models.CharField(max_length=255, verbose_name='Last name')

    def __str__(self):
        return f'{self.name} {self.surname}'


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Title')

    def __str__(self):
        return self.title


class User(models.Model):
    login = models.CharField(max_length=255, verbose_name='Login')
    name = models.CharField(max_length=255, verbose_name='Name', blank=True)

    def __str__(self):
        return str(self.name)


class Comments(models.Model):
    text = models.TextField(max_length=300, verbose_name='Text', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, verbose_name='Use', on_delete=models.CASCADE)

    def __str__(self):
        return self.text if self.text else str(self.text)
