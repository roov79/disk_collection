from django.db import models
import datetime
from django.utils.dateparse import parse_date

# GENRES_OP = [
#     ('action', 'Action'),
#     ('drama', 'Drama'),
#     ('sci_fi', 'Sci-Fi'),
#     ('anime', 'Anime'),
# ]

class Disks(models.Model):
    title = models.CharField(max_length=150)
    released_date = models.DateField(default=None)
    production = models.CharField(max_length=50)
    prod_type = models.CharField(max_length=30)
    genres = models.CharField(max_length=255, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)