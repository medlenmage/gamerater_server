from rest_framework import serializers
from gameraterapi.models import GameReview



class GameReviewSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for games

    Arguments:
        serializers
    """
    class Meta:
        model = GameReview
        url = serializers.HyperlinkedIdentityField(
            view_name='game_review',
            lookup_field='id'
        )
        fields = ('id', 'user', 'game', 'review')