"""Models for posts application."""

from django.db import models


class Post(models.Model):
    """Model for a blog post."""

    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    markdown_content = models.TextField()

    def __str__(self):
        """Text representation of blog post.

        Returns:
            Title attribute of Post (str).
        """
        return self.title
