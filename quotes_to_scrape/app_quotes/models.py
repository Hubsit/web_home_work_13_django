from django.db import models


# Create your models here.
class Tag(models.Model):
    tag = models.CharField(max_length=50, unique=True, null=False)

    def __str__(self):
        return f'{self.tag}'


class Author(models.Model):
    fullname = models.CharField(max_length=50, null=False)
    born_date = models.CharField(max_length=20)
    born_location = models.CharField(max_length=100)
    description = models.CharField(max_length=5000)

    def __str__(self):
        return f'{self.fullname}'


class Quote(models.Model):
    quote = models.CharField(max_length=1000, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.quote}'

