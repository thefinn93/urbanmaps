from django.db import models

class MapPoint(models.Model):
    title = models.CharField(max_length=50)
    pub_date = models.DateTimeField('date published')
    description = models.CharField(max_length=5000)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
