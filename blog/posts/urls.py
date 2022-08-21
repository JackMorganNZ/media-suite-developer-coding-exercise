from django.urls import path
from posts import views

app_name = 'posts'

urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    # path('<slug:slug>/', views.post, name='post'),
]
