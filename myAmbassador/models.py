from django.db import models


class Link(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    clicks = models.IntegerField()
