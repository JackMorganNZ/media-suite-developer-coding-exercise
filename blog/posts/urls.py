from django.urls import path
from posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('<slug:post_slug>/', views.PostView.as_view(), name='post'),
]
