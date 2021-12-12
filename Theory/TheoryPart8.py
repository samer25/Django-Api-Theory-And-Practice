"""
Django DRF Image Uploading
Uploading images from the front-end to backend RESTful API

djanog coverage
Build views / URLs to handle uploading
"""

"""
First we need to install pillow because we nee to utilizing and 
manipulating images so on pillow going to allow us to do it 

pip install pillow

we have to create new folder in our project 'media or images'
here we are going to save all images that we upload
and that will going to be served to a front-end

now to settings.py
lets import os 
now we have to tell django where is the media folder is 
to know where to save the images

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # we are getting the path where is the media directory 
MEDIA_URL = '/media/'

We are going to use media url when we request items from
django to direct the url to the media folder
so that we can access the images from the web

we can do to serve media files locally
in project/urls.py 
going to import settings and static 

from django.conf import settings
from django.conf.urls.static import static

and now let defining that we are utilizing a media folder

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

that is going to allow us to work with media folder locally

now lets go to blog/models.py
and lets add to Post model image field 

image = models.ImageField('Image', upload_to=upload_to, default='posts/default.jpg')

the default image is when someone doesnt upload image will have default image
in folder media must have posts/default.jpg to work 
in upload_to we are going to define a function upload_to
outside of classes lets create a function to specify where to upload the images

def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)

taking the instance so the instance we building a post i then press submit
that's the instance that information 
and then the filename 
unfortunately we can't use the post id in this instance
because this is being performed before the data is saved

now let add it to our serializer
in blog_api.serializer.py

and in class PostSerializer add in fields image

now we are going to views,py
and lets create new CreatePost (remove the old one)
we will use APIView in this case

class CreatePost(APIView):
    permission_classes = [IsAuthenticated]
    parser_classes = [MultiPartParser, FormParser]
    
    to upload images and text there is a multiple 
    part data (multiple part of data) that's being
    uploaded we need to be able to handle that 
    so for that we use parser_classes
    if we want to upload only file we can use FileUploadParser
    but now we not doing that because we are uploading files and text
      
    now lets create method post to handle when we post a new items
     
    def post(self, request, format=None):
        now let take a data from request
        serializer = PostSerializer(data=request.data)
         now lets check if serializer data is valid
         and if it to save it 
         if serializer.is_valid():
            serializer.save()
            and now lets return a response
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            

    lets turn of DEFAULT_AUTHENTICATION_CLASSES in settings.py
    and in views class create post comment the permission_classes
    just to be easier to test this in Postman
    
"""