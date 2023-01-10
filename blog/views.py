from rest_framework import generics
from blog.models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser


class CategoryList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostUserWritePermission(BasePermission):
    """
    Object level permissions for User
    """
    message = 'Warning! Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class PostList(generics.ListCreateAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
