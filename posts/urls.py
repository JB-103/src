from django.urls import path
from django.views.generic import RedirectView
from .views import (
    post_list_and_create,
    load_post_data_view,
    like_unlike_post,
    post_detail,
    post_detail_data_view,
    delete_post,
    update_post,
    image_upload_view,

)

app_name = 'posts'

urlpatterns = [
    path('', post_list_and_create, name='main-board'),
    path('like-unlike/', like_unlike_post, name='like-unlike'),
    path('upload/', image_upload_view, name='image-upload'),
    path('<pk>/', post_detail, name='post_detail'),
    path('<pk>/update/', update_post, name='post_update'),
    path('<pk>/delete/', delete_post, name='post_delete'),

    path('data/<int:num_posts>/', load_post_data_view, name='posts-data'),
    path('<pk>/data/', post_detail_data_view, name='post_detail_data'),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
]
