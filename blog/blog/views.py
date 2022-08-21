from django.views.generic.base import RedirectView


class HomeRedirectView(RedirectView):

    pattern_name = 'posts:home'
    permanent = False
    query_string = True
