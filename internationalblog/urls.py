from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:post_id>/', views.post, name='post'),
    path('new-post/', views.new_post, name='new_post'),
    path('new-post/add-post/', views.add_post, name='add_post'),
    path('thanks/', views.thanks, name='thanks'),
]