from django.db import models

# Create your models here.

class Setting(models.Model):
    title = models.CharField(max_length=100)
    keywords = models.CharField(max_length=255)
    description = models.TextField(max_length=500)
    phone = models.CharField(max_length=500)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=100)
    smpt_sever = models.CharField(max_length=300)
    smpt_email = models.CharField(max_length=300)
    smpt_password = models.CharField(max_length=300)
    smpt_port = models.CharField(max_length=300)
    youtube = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    icon = models.CharField(max_length=300)
    aboutus = models.CharField(max_length=300)
    contact = models.CharField(max_length=300)

    def __str__(self):
        return self.title
