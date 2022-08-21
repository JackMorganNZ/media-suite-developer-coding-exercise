from django.views import generic
from posts.models import Post


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
