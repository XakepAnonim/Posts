from django.urls import path

from .views import *

urlpatterns = [
    path('posts/', posts, name='posts'),
    path('posts/add/', add_post, name='add_post'),
    path('posts/<int:post_id>/edit/', edit_post, name='edit_post'),
    path('posts/<int:post_id>/delete/', delete_post, name='delete_post'),

    path('posts/popular/', popular_posts, name='popular_posts'),
    path('posts/latest/', latest_posts, name='latest_posts'),
    path('posts/<int:post_id>/', post_details, name='post_details'),
    path('posts/<int:post_id>/comments/', post_comments, name='post_comments'),
    path('posts/<int:post_id>/likes/', post_likes, name='post_likes'),

    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),

    path('access/', access, name='access'),
    path('json/', json_page, name='json_page'),

    path('set_cookie/', set_cookie, name='set_cookie'),
    path('get_cookie/', get_cookie, name='get_cookie'),
]

handler404 = 'shop.views.page_not_found'