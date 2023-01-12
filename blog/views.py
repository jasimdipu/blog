from rest_framework import generics, viewsets
from blog.models import Post, Category
from .serializers import PostSerializer, CategorySerializer
from rest_framework.permissions import SAFE_METHODS, BasePermission, IsAdminUser


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PostUserWritePermission(BasePermission):
    """
    Object level permissions for User
    """
    message = 'Warning! Creating and Editing posts is restricted to the author only.'

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
