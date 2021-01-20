from rest_framework import viewsets
from gameraterapi.models import Category
from gameraterapi.serializers.categorySerializer import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer