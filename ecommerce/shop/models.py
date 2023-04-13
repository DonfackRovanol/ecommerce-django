from email.mime import image
from turtle import title
from unicodedata import category, name
from django.db import models
from django.forms import CharField

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date_added']
    
    def __str__(Self):
        return Self.name
    

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    description = models.TextField()
    category = models.ForeignKey(Category, related_name='categorie', on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True,upload_to='images/')
    date_added = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date_added']
    
    def __str__(Self):
        return Self.title


class Commande(models.Model):
    item = models.CharField(max_length=300)
    total = models.CharField(max_length=200)
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=200)
    zipcode = models.CharField(max_length=300)
    date_commande = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-date_commande']
        
    def __str__(Self):
        return Self.nom
