from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=150, unique=True)
    password = models.CharField(max_length=100)
    city = models.CharField(max_length=70)

    def __str__(self):
        return self.name
