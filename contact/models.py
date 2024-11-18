from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=254)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=30, null=True, blank=True)
    topic = models.CharField(max_length=30)
    message = models.TextField(max_length=254)
    upload = models.FileField(upload_to="uploads/", null=True, blank=True)

    def __str__(self):
        return f"{self.topic}|{self.name}"