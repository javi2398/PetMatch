from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=100)
    species = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name
