from django.db import models


# Create your models here.
class Algorithm(models.Model):
    name = models.TextField()
    classify = models.TextField()

    class Meta:
        db_table = 'algorithm'
