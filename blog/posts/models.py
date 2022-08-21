"""Models for posts application."""

from django.db import models
from django.urls import reverse
from markdown2 import Markdown
from posts.utils import update_tags


class Post(models.Model):
    """Model for a blog post."""

    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=500)
    author = models.CharField(max_length=500)
    markdown_content = models.TextField()
    html_content = models.TextField(default='')

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

    def save(self, *args, **kwargs):
        markdowner = Markdown()
        self.html_content = markdowner.convert(self.markdown_content)
        update_tags(self)
        super(Post, self).save(*args, **kwargs)


class Tag(models.Model):
    """Model for a blog post tag."""

    slug = models.SlugField(unique=True)
    name = models.CharField(max_length=200)
    posts = models.ManyToManyField(
        Post,
        related_name="tags"
    )
