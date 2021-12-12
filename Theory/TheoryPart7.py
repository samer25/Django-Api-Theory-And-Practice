"""

Django Simple CRUD with DRF

Django Coverage:
Build views/ URls to handle CRUD requests
"""

"""
First we need view to create new posts

class CreatePost(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
now we have simple view to create a post

now we want a detail post

class AdminPostDetail(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
now the Edit post

class EditPost(generics.UpdateAPIView, PostUserWritePermission):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer



now the delete post

class DeletePost(generics.RetrieveDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    

now lets add some urls

path('admin/create/', CreatePost.as_view(), name='create_post'),
path('admin/edit/post-detail/<int:pk>/', AdminPostDetail.as_view(), name='admin_detail_post'),
path('admin/edit/<int:pk>/', EditPost.as_view(), name='edit_post'),
path('admin/delete/<int:pk>/', DeletePost.as_view(), name='delete_post'),

"""
