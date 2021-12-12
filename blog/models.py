from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
from users.models import NewUser


def upload_to(instance, filename):
    return 'posts/{filename}'.format(filename=filename)


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
     category foreignkey we are using on on_delete Protect that we ensure that
     if anyone tries to delete any categories it has no effect on the post
     actual fact it won't allow you to delete the category in this case
     so for that we are using .PROTECT
     """
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250, unique=True)
    image = models.ImageField('Image', upload_to=upload_to, default='posts/default.jpg')
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.SlugField(max_length=250, unique_for_date='published')
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(NewUser, on_delete=models.CASCADE, related_name='blog_posts')

    """
    creating status choice that can choice to be publish or in draft
    so we needs to be a facility where we can put it into a draft mode
    so that only posts that are publish will show 
    """
    """
    we have to create new model manager that by default we want to return
    filtered data that to show only published post (that can be done in view also)
    for that we creating custom manager here so be default if instead of running
    .objects.all() on the data when we make a query we can run post.objects
    and that's going to utilize this filter that will select only data that has got 
    states of published 
    """

    class PostObject(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    status = models.CharField(max_length=10, choices=options, default='published')
    """
    Now we can specify the different model managers
    objects is going to be the default model manager that we can utilize and the 
    post_objects is the custom manager 
    """
    objects = models.Manager()  # default manager
    post_objects = PostObject()  # custom manager

    """
    Now by default we want to display a data either in ascending or descending order
    by published(date when was created)
    """

    class Meta:
        ordering = ('-published',)  # descending order

    def __str__(self):
        return self.title
