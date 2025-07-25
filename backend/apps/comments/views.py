from rest_framework import generics
from rest_framework.generics import CreateAPIView

from .models import CommentModel
from .serializer import CommentSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer

class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer


class CommentCreateAPIView(CreateAPIView):
    queryset = CommentModel.objects.all()
    serializer_class = CommentSerializer