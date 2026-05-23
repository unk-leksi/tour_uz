from django.db import models


class Excursion(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    image = models.ImageField(upload_to='excursions_images/')
    duration = models.IntegerField()

    def __str__(self):
        return self.title
