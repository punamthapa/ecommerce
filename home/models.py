from django.db import models

# Create your models here.
STATUS = (('active', 'active'), ('passive', 'passive'))
LABEL = (('new', 'new'), ('hot', 'hot'), ('sale', 'sale'), ('', 'default'))

class Category(models.Model):
    name = models.CharField(max_length=300)
    image = models.CharField(max_length=300)
    slug = models.CharField(max_length=300, unique=True)
    status = models.CharField(choices=STATUS, max_length=300)

    def __str__(self):
        return self.name

class Slider(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    status = models.CharField(choices=STATUS, max_length=200)

    def __str__(self):
        return self.name

class Ad(models.Model):
    name = models.CharField(max_length=300)
    rank = models.IntegerField()
    image = models.ImageField(upload_to='media')
    description = models.TextField(blank=True)
    status = models.CharField(choices=STATUS, max_length=300)

    def __str__(self):
        return self.name

class Brand(models.Model):
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    status = models.CharField(choices=STATUS, max_length=300)

    def __str__(self):
        return self.name

class Item(models.Model):
    title = models.CharField(max_length=300)
    price = models.IntegerField()
    discounted_price = models.IntegerField(default=0)
    label = models.CharField(choices=LABEL, max_length=200)
    image = models.ImageField(upload_to='media')
    status = models.CharField(choices=STATUS, max_length=300)
    slug = models.CharField(max_length=200, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title