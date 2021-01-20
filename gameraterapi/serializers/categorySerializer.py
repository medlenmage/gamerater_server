from rest_framework import serializers
from gameraterapi.models import Category

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    """JSON serializer for games

    Arguments:
        serializers
    """
    class Meta:
        model = Category
        url = serializers.HyperlinkedIdentityField(
            view_name='category',
            lookup_field='id'
        )
        fields = ('id', 'name')