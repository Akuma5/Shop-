from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Magazine, MagazineLike, MagazineComment
from .permissions import IsAdminOrReadOnly
from .serializers import MagazineSerializers, MagazineCommentSerializer, MagazineUpdateSerializers
from django_filters.rest_framework import DjangoFilterBackend


class MagazineAPIListPagination(PageNumberPagination):
    page_size = 3
    page_query_param = 'page_size'
    max_page_size = 10000


class MagazineAPIList(generics.ListCreateAPIView):
    queryset = Magazine.objects.all()
    serializer_class = MagazineSerializers
    permission_classes = (IsAuthenticatedOrReadOnly, )
    pagination_class = MagazineAPIListPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['cat']
    search_fields = ['title', 'id']


class MagazineAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Magazine.objects.all()
    serializer_class = MagazineUpdateSerializers
    permission_classes = (IsAuthenticated,)


class MagazineAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Magazine.objects.all()
    serializer_class = MagazineUpdateSerializers
    permission_classes = (IsAdminOrReadOnly,)


class MagazineLikeView(APIView):
    """ Добавляет лайк """

    def get(self, request, product_pk):
        created = MagazineLike.objects.filter(product_id=product_pk, user=request.user).exists()
        if created:
            MagazineLike.objects.filter(
                product_id=product_pk,
                user=request.user
            ).delete()
            return Response({'success': 'unliked'})
        else:
            MagazineLike.objects.create(product_id=product_pk, user=request.user)
            return Response({'success': 'liked'})


class CommentView(ModelViewSet):
    """ Добавляет коммент """
    queryset = MagazineComment.objects.all()
    serializer_class = MagazineCommentSerializer
    lookup_field = 'pk'



