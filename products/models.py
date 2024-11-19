from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class Platform(models.Model):
    name = models.CharField(max_length=64, unique=True)    
    def __str__(self):
        return self.name


class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
        
    name = models.CharField(max_length=254, unique=True)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Game(models.Model):
    title = models.CharField(max_length=254, unique=True)
    slug = models.SlugField(max_length=254, null=True)
    genre = models.CharField(max_length=64)
    platform = models.ForeignKey(Platform, null=True, on_delete=models.SET_NULL)
    age_rating = models.IntegerField(null=True)
    developer = models.CharField(max_length=32)
    publisher = models.CharField(max_length=32)
    release = models.DateField()

    def __str__(self):
        return f"{self.title}"


class Console(models.Model):
    title = models.CharField(max_length=254, unique=True)
    slug = models.SlugField(max_length=254, unique=True)
    developer = models.CharField(max_length=32, null=True)
    release = models.DateField()
    manufacturer = models.CharField(max_length=32, null=True)
    platform = models.ForeignKey(Platform, null=True, on_delete=models.SET_NULL)
    processor = models.CharField(max_length=254, null=True)
    graphics = models.CharField(max_length=254, null=True)
    memory = models.CharField(max_length=254, null=True)
    storage = models.CharField(max_length=254, null=True)
    sound = models.CharField(max_length=254, null=True)
    mass = models.CharField(max_length=254, null=True)

    def __str__(self):
        return f"{self.title}"


class Product(models.Model):
    category = models.ForeignKey(Category, null=True, on_delete=models.SET_NULL)
    game = models.OneToOneField(Game,on_delete=models.SET_NULL, related_name="product", null=True, blank=True)    
    console = models.OneToOneField(Console, on_delete=models.SET_NULL, related_name="product", null=True, blank=True)    
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    cover = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name

    def get_price(self):
        return self.price + "€"

    
