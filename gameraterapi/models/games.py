from django.db import models
from django.db.models.deletion import CASCADE

class Game(models.Model):
    title = models.CharField(max_length=75)
    designer = models.CharField(max_length=50)
    year_released = models.TextField()
    number_of_players = models.IntegerField()
    estimated_time_play = models.TextField()
    age_recommendation = models.TextField()
    category = models.ForeignKey("Category",
        on_delete=CASCADE,
        related_name="categories",
        related_query_name="category"
    )
