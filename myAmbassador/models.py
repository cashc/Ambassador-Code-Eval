from django.db import models


class Link(models.Model):

    id = models.AutoField(primary_key=True)
    title = models.TextField()
    clicks = models.IntegerField(default=0)
