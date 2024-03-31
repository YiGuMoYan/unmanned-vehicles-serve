from django.db import models


# Create your models here.
class Map(models.Model):
    name = models.TextField()
    video = models.TextField()
    classify = models.TextField()
    algorithm = models.TextField()

    class Meta:
        db_table = 'map'
