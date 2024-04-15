from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth import get_user_model
class Dishes(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    Preparation_methods = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)


class Chefs(models.Model):
    name = models.CharField(max_length=100)
    Culinary_Background = models.TextField()
    Profession = models.TextField()

class Rating(models.Model):
    dish = models.ForeignKey('Dishes', related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), related_name='ratings', on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

    class Meta:
        unique_together = ('dish', 'user')

