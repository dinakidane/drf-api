from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from likes.model import Like
from likes.serializer import LikeSerializer

class LikeList(generics.ListCreateAPIView):
    serializers_class = LikeSerializer
    permission_class = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class LikeDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()



