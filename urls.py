from django.urls import path
from .views import PostListAPIView, PostDetailAPIView, PostDeleteAPIView,PostUpdateAPIView,PostCreateAPIView
    # , PostUpdateAPIView, PostDeleteAPIView, PostCreateAPIView

app_name = 'api'

urlpatterns =[
    path('',PostListAPIView.as_view(),name = 'list'),
    path('create', PostCreateAPIView.as_view(), name='create'),
    path('<slug>', PostDetailAPIView.as_view(),name = 'detail'),
    path('edit/<slug>',PostUpdateAPIView.as_view(),name = 'edit'),
    path('delete/<slug>',PostDeleteAPIView.as_view(),name = 'delete'),
]