
from rest_framework import serializers
from blog.models import Post
from django.conf import settings


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'excerpt', 'content', 'status')
