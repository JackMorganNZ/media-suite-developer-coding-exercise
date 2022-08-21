from django.urls import path
from posts import views
from rest_framework import routers


app_name = 'posts'

router = routers.DefaultRouter()
router.register(r'posts', views.PostAPIViewSet)

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('<slug:post_slug>/', views.PostView.as_view(), name='post'),
]
