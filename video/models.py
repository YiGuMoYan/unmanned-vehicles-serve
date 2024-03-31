from django.db import models


# Create your models here.
class Video(models.Model):
    name = models.TextField()
    md5 = models.TextField()

    class Meta:
        db_table = 'video'


class Document(models.Model):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='static/', null=True, blank=True)
