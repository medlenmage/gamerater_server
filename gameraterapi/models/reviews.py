from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey

class Review(models.Model):
    player = models.ForeignKey( "Player",
        on_delete=CASCADE,
        related_name="reviews",
        related_query_name="review"
    )
    game = models.ForeignKey( "Game", 
        on_delete=CASCADE,
        related_name="reviews",
        related_query_name="review"
    )
    review = models.TextField()
    datestamp = models.DateTimeField()
