from django.db import models
from django.db.models.deletion import CASCADE

class Review(models.Model):
    player = models.ForeignKey( "Player",
        on_delete=CASCADE,
        related_name="players",
        related_query_name="player"
    )
    game = models.ForeignKey( "Game", 
        on_delete=CASCADE,
        related_name="players",
        related_query_name="player"
    )
    review = models.TextField()
    rating = models.IntegerField()
