from django.db import models

# Create your models here.


class UserProfile(models.Model):
    # image = models.FileField(upload_to="images")
    image = models.ImageField(upload_to="images") # for image field you need to install Pillow