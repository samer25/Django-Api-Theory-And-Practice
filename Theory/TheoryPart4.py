"""
Viewsets and routers

A fleeting introduction to combining views and using
automatic URL pattern generation

Django Coverage

Gentle introduction to viewsets
Gentle introduction to Routers
Building a single post or detail view
"""
"""
Problem

As the project scales:
-Increasingly large amount of views
    -Endpoints(URLs) subsequently scales with views
    -Repetition of code in the views(queryset)
-Multiple endpoints (URLs) can become difficult to
maintain (larger projects) 
"""
"""
Viewsets

Can speed-up API development
Additional layer of abstraction
-Views
A single viewset can replace multiple (related) views
Repeated logic can be combined into a single class
Combined logic for a set of related views in a single class(viewset)
Write less code - Promotes DRY


Lets turn off the DEFAULT_AUTHENTICATION_CLASSES BY COMMENT IT that we can work 
in the frontend (api view django)  

View set:
-viewsets.ViewSet
-Simply a type of class-based View
-Does not provide as .get() or .post()
-Provides actions such as .list() . create()
-Method handlers for a ViewSet are bound to the corresponding actions
 
Different options in view set methods:

    # def list(self, request):
    #     pass

    # def create(self, request):
    #     pass

    # def retrieve(self, request, pk=None):
    #     pass

    # def update(self, request, pk=None):
    #     pass

    # def partial_update(self, request, pk=None):
    #     pass

    # def destroy(self, request, pk=None):
    #     pass
    
now let go to blog_api/views.py and comment the classes
and import the viewsets

from rest_framework import viewsets

class PostList(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Post.post_objects.all()
    
    def list(self, request):
        serializer_class = PostSerializer(self.queryset, many=True)
        return Response(serializer_class.data)
        
    That is a simple way to return a list serializer utilizing viewset

    The view set doesn't necessarily work with get and post
    but the meaningful action is translated into one of these 
    functions in viewsets so if we sent across a post request
    obviously we would be asking to create something(def create())
    therefore this build create method  which deals with all that
    functionality
    
    def retrieve(self, request, pk=None):
        "It retrieve something from the database normally a single item "
        "It is similar with generics.RetrieveAPIView"
        post = get_object_or_404(self.queryset, pk=pk)
        serializer_class = PostSerializer(post)
        return Response(serializer_class.data)
    
So at moment when we try this out it wont work because there's a conflict
now the urls that we create wont work with this implementation
so this is where router comes in

Routers:
Automatically generate URL patterns from the developer
Routes for create/retrieve/update/destroy style actions

The routes can be overwritten and we can apply individual roots

Now let go to blog_api/urls.py
and remove the urlpatterns variable and PostDetail that we imported from views.py
then import DefaultRouter:

form .views import PostList
from rest_framework.routers import DefaultRouter

app_name = 'blog_api'

router = DefaultRouter() # we bring in the DefaultRouter into a variable so we can access it
# now we are going to make a new url

router.register('', PostList, basename='post)

# now we tell django that we are not using url patterns anymore 
# and now the router will take over the url
urlpatterns = router.urls

now we can go to browser and check it with /api/ and api/1 or whatever id exist
if we just put wrong url we can see the urls that router create like api/sasd/dsfs
and that will show:
admin/
api/ ^$ [name='posts-list']
api/ ^\.(?P<format>[a-z0-9]+)/?$ [name='posts-list']
api/ ^(?P<pk>[^/.]+)/$ [name='posts-detail']
api/ ^(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='posts-detail']
api/ ^$ [name='api-root']
api/ ^\.(?P<format>[a-z0-9]+)/?$ [name='api-root']
api/token/ [name='token_obtain_pair']
api/token/refresh/ [name='token_refresh']
api/users/
"""

"""
Let check the ModelViewSet

lets comment The PostList and create new PostList with ModelViewSet
 
class PostList(viewsets.ModelViewSet):
    permission_classes = [PostUserWritePermission]
    serializer_class = PostSerializer
    queryset = Post.post_objects.all()
    
That is all what we need to write that create all methods that we need
(list(), create(), retrieve(), destroy(), update(), ...) 
so this takes us to another level of abstraction 
So some times this become a problem when once we start customising
or we want something different from default
Check it in browser

We can extent it probably we what two things to extend here
one is to utilize a different query set
we can define a custom queryset   
    
    # Define Custom Queryset
    def get_queryset(self):
        return Post.objects.all()

"""

"""
Now we are going to build the functionality 
when we type in the browser in example category "django"
and that will take us in all django category post that is created

first will get a single object by id we need to overwrite the get_object() in class PostList

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get('pk')
        return get_object_or_404(Post, title=item) 
        # we will not use number because in router urls there api/ ^(?P<pk>[^/.]+)\.(?P<format>[a-z0-9]+)/?$ [name='posts-detail']
        # that takes letters and numbers [a-z0-9]
        
and comment queryset because we using get_queryset()
now we can use title to access the individual post
when we go to route directory get_queryset() will fired off
when we type in a post name into the url get_object() will fired off 
now lets go and test it

go first to /api/
and now lets take a title from the post and past it in urls /api/django 
if there more that one title with the same title will get an error
for that change in the module Post title to unique=True
"""
