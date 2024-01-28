from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


# Create your models here.
class Items(models.Model):
    DEF_IMG = 'https://static.wixstatic.com/media/bf242e_6133b4ae6a104cc2b50d70179f35efea~mv2.jpg/v1/fill/w_500,h_376,al_c,lg_1,q_80,enc_auto/food-placeholder.jpg'
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             null=True, blank=True)
    items_name = models.CharField(max_length=256)
    items_desc = models.CharField(max_length=256)
    items_price = models.FloatField()
    items_image = models.CharField(max_length=600,
                                   default=DEF_IMG)

    def __str__(self) -> str:
        return self.items_name

    def get_absolute_url(self):
        return reverse('food:details', kwargs={"pk": self.pk})
