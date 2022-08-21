from django.views import generic
from posts.models import Post
from rest_framework import viewsets
from posts.serializers import PostSerializer


class IndexView(generic.ListView):
    """View for the posts application homepage."""

    template_name = 'posts/index.html'
    context_object_name = 'posts'
    model = Post


class PostView(generic.DetailView):
    """View for a specific post."""

    model = Post
    template_name = 'posts/post.html'
    slug_url_kwarg = 'post_slug'


class PostAPIViewSet(viewsets.ReadOnlyModelViewSet):
    """API endpoint that allows questions to be viewed."""

    queryset = Post.objects.all()
    serializer_class = PostSerializer
