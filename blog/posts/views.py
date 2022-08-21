from django.views import generic
from posts.models import Post


class IndexView(generic.ListView):
    """View for the posts application homepage."""

    template_name = 'posts/index.html'
    context_object_name = 'posts'
    model = Post
