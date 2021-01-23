from rest_framework import viewsets
from gameraterapi.models import GameReview
from gameraterapi.serializers import GameReviewSerializer

class GameReviewViewSet(viewsets.ModelViewSet):
    queryset = GameReview.objects.all()
    serializer_class = GameReviewSerializer