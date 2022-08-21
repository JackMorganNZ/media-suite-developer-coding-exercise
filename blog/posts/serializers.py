"""Serializers for posts models."""

from rest_framework import serializers
from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    """Serializer for a post."""

    class Meta:
        """Meta settings for serializer."""

        model = Post
        fields = (
            'slug',
            'title',
            'author',
            'markdown_content',
        )
