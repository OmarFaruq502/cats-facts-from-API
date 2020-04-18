from django.db import models

# Create your models here.
class Fact(models.Model):
    fact = models.CharField('fact', max_length = 700)

    def __str__(self):
        return self.fact