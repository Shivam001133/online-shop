from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='user.jpg',
                              upload_to='profile_icon.png')
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.user.username
