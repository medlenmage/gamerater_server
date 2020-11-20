from django.db import models
from django.db.models.deletion import CASCADE

class Game(model.models):
    title = models.CharField(max_length=75)
    description = models.CharField(max_length=150)
    designer = models.CharField(max_length=50)
    year_released = models.IntegerField()
    number_of_players = models.IntegerField()
    estimated_time_play = models.IntegerField()
    age_recommendation = models.IntegerField()
    category = models.ForeignKey("Categories",
        on_delete=CASCADE,
        related_name="categories",
        related_query_name="category"
    )
