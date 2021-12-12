"""
Django coverage:

Basic Filter methods
Filtering by URL
Custom overrides (get_object)
DjangoFilterBackend
filters.SearchFilter
"""

"""
First lets return the generic API view and remove the viewsets

and in urls let return the urlpatterns 

urlpatterns = [
    path('<int:pk>/', PostDetail.as_view(), name='detail_create'),
    path('', PostList.as_view(), name='list_create'),
]
"""

"""
Lets remove queryset from PostList and add method get_queryset that we can customise

    def get_queryset(self):
        user = self.request.user
        return Post.objects.filter(author=user)
        
That will show the user posts only if the user had created a post

check it when you go to api/ will show the user post that is login

That is a simple filter tht can be use like instagram profile to see your post that you posted

now lets make example #2 
Filtering against the URL (ID)
Get post based on title / string

we need to remove queryset
that is just for example of filter that we make 
    def get_queryset(self):
        slug = self.kwargs['pk']
        return Post.objects.filter(slug=slug)

then change the urls.py of PostDetail

path('posts/<str:pk>/', PostList.as_view()),

we are specify the data type with srt 
this is just a reference name which we can utilize 
to send across the data and reference it in the view

sometimes we create search facilities in our application
and create variables in our url like:
/?slug=post1

if we wanted to get to this data we need to reference 
it by slug
also we might have multiple deep queries:
/?slug=post1+sf+sdfs+fsd+fsd+fs+dfsd+

typically this can see from a search engine for example

In django can take and utilize it by

    class PostDetail(generic.RetrieveAPIView):
        serializer_class = PostSerializer
        
        def get_queryset(self):
            slug = self.request.query_params.get('slug', None)
            Now we collect data from url
            if we work this way we dont need to define in urls the data like(<int:pk>)
            we can remove it 
            now we asking it to read it on this variable that we created (slug)
            and we specify what data to get (get('slug', None))
            we will take the data from the slug item 
            in url (/?slug=post1) the slug data is after = this mean post1 is the data 
            
            now we can run a query like a normal 
            return Post.objects.filter(slug=slug)            
            but to work we have to use generic.ListAPIView
            
            
            we can utilize multiple items that is possible but there are better tools
            that we can do that 
            django-filter package is great example 
            
            pip install django-filter
            
            then we have to add it in INSTALLED_APPS
            
            in view lets import it 
            
            from rest_framework import filters
            
            them lets create class
            
            class PostListDetailFilter(generics.ListAPIView):
                queryset = Post.objects.all()
                serializer_class = PostSerializer
                filter_backends = [filters.SearchFilter]
                
                this will work in very much similar to what we had before
                where we use the endpoint and then we use the question mark 
                to build a structured format to take in different parameters
                and then run a filter based upon those parameters 
                here is more detailed and there's more options
                with this search capabilities comes these new tools:
                
                # '^' Starts-with search.
                # '=' Exact matches.
                # '@' Full-text search. (Currently only supported Django's PostgreSQL backend.)
                # '$' Regex search.
                
                we have to specify what we want to search we are using slug
                
                search_fields = ['^slug']
                
                this is start with we are utilizing the top hat here
                and we need an endpoint 
                in urls let create endpoint
                path('search/custom/', PostListDetailFilter.as_view(), name='post_search')
                lets try it 
                so if we use the old method /?slug=django wont work 
                we have to use key word search:
                /?search=django and will show all that mach data have value "django"
                
"""
