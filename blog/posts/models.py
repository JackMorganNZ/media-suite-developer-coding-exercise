"""Models for posts application."""

from django.db import models
from django.urls import reverse


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

    def get_absolute_url(self):
        """Return the canonical URL for a post.

        Returns:
            URL as string.
        """
        kwargs = {
            'post_slug': self.slug
        }
        return reverse('posts:post', kwargs=kwargs)
