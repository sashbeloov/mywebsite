from django.db import models

# Create your models here.

class Setting(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    phone = models.CharField(max_length=500)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    smtp_server = models.CharField(blank=True,max_length=50)
    smtp_email = models.CharField(blank=True,max_length=50)
    smtp_password = models.CharField(blank=True,max_length=10)
    smtp_port = models.CharField(blank=True,max_length=5)
    youtube = models.URLField(blank=True, max_length=50)
    instagram = models.URLField(blank=True, max_length=50)
    facebook = models.URLField(blank=True, max_length=50)
    icon = models.ImageField(blank=True, upload_to='images/')
    aboutus = models.CharField(max_length=300)
    contact = models.CharField(max_length=300)

    def __str__(self):
        return self.title
