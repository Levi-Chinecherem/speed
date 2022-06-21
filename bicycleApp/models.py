from django.db import models

# Create your models here.
class Subscriber(models.Model):
    email = models.EmailField(null=False)

    def __str__(self):
        return self.email


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    message = models.TextField()

    def __str__(self):
        return self.name