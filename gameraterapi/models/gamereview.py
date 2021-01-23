from django.db import models
from django.db.models.deletion import CASCADE
from django.conf import settings
from django.db import models
from django.db.models.fields import related


class GameReview(models.Model):
    user = models.ForeignKey("User", related_name="reviews", related_query_name="review", on_delete=CASCADE, default=1)
    game = models.ForeignKey("Game", related_name="reviews", related_query_name="review", on_delete=CASCADE, default=1)
    review = models.TextField()
