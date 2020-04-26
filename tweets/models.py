from django.db import models


class Tweets(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField(null=True, blank=True)
    image = models.FileField(upload_to='img/', null=True, blank=True)
