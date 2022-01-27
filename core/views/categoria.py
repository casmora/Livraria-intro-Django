from rest_framework.viewsets import ModelViewSet
#from rest_framework.permissions import IsAuthenticated
from core.models import Categoria
from core.serializers import CategoriaSerializer


class CategoriaViewSet(ModelViewSet):
    #permission_classes = [IsAuthenticated]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
