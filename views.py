from rest_framework.generics import ListAPIView,RetrieveAPIView,RetrieveDestroyAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter,OrderingFilter
from ..models import Post
from .serializers import PostListSerializer, PostCreateEditeSerialzier, PostDeleteDetailSerialzier
from .permissions import IsOwnerOrReadOnly
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination

class PostListAPIView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer
    filter_backends = [SearchFilter,OrderingFilter]
    pagination_class = PageNumberPagination
    search_fields = ('title', 'content','user__id')

    def get_queryset(self,*args,**kwargs):
        queryset_list = Post.objects.all()
        query = self.request.GET.get('q')
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query)|
                Q(content__icontains=query)|
                Q(user__first_name__icontains=query)|
                Q(user__last_name__icontains=query)
            )
        return queryset_list


class PostDetailAPIView(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDeleteDetailSerialzier
    lookup_field = 'slug'

class PostUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateEditeSerialzier
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    lookup_field = 'slug'

    def perform_update(self,serializer):
        serializer.save(user = self.request.user)

class PostDeleteAPIView(RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostDeleteDetailSerialzier
    lookup_field = 'slug'

class PostCreateAPIView(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateEditeSerialzier
    permission_classes = [IsAuthenticated]
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

