from django.db import models


class Stat(models.Model):
    name = models.CharField(max_length=250)
    born = models.CharField(max_length=250)
    nationality = models.CharField(max_length=100)
    height = models.CharField(max_length=200)
    weight = models.CharField(max_length=200)
    nba_draft = models.CharField(max_length=250)

    def __str__(self):
        return self.name
