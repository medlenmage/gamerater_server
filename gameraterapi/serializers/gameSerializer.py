from rest_framework import serializers
from gameraterapi.models import Game



class GameSerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for games

    Arguments:
        serializers
    """
    class Meta:
        model = Game
        url = serializers.HyperlinkedIdentityField(
            view_name='game',
            lookup_field='id'
        )
        fields = ('id', 'title', 'designer', 'year_released', 'number_of_players', 'estimated_time_play', 'age_recommendation', 'category')