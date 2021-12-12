from django.urls import path
from rest_framework.routers import DefaultRouter

from blog_api.views import PostList, PostDetail, PostListDetailFilter, CreatePost, AdminPostDetail, EditPost, DeletePost

app_name = 'blog_api'

# router = DefaultRouter()
#
# router.register('', PostList, basename='posts')
# urlpatterns = router.urls


urlpatterns = [
    # path('posts/', PostDetail.as_view(), name='detail_create'),
    path('post/<str:pk>/', PostDetail.as_view(), name='detailpost'),
    path('', PostList.as_view(), name='list_create'),
    path('search/', PostListDetailFilter.as_view(), name='post_search'),
    path('admin/create/', CreatePost.as_view(), name='create_post'),
    path('admin/edit/post-detail/<int:pk>/', AdminPostDetail.as_view(), name='admin_detail_post'),
    path('admin/edit/<int:pk>/', EditPost.as_view(), name='edit_post'),
    path('admin/delete/<int:pk>/', DeletePost.as_view(), name='delete_post'),

]
