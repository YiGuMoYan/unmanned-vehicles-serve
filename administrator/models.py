from django.db import models


# Create your models here.
class Administrator(models.Model):
    username = models.TextField()
    password = models.TextField()

    class Meta:
        db_table = "admin"
