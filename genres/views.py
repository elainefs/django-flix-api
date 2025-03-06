from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Genre
from .permissions import GenrePermissionClass
from .serializers import GenreSerializer


class GenreCreateListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, GenrePermissionClass]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class GenreRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, GenrePermissionClass]
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
