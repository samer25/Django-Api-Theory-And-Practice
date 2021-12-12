from django.test import TestCase
from django.contrib.auth.models import User
from blog.models import Post, Category


# Create your tests here.

class TestCreatePost(TestCase):

    @classmethod
    def setUpTestData(cls):
        """
        First we have to create data for the models the Post will be last to create
        because we have first to create User and Category for be enable to create
        Post because we have foreignkeys in Post
        """
        test_category = Category.objects.create(name='django')  # creating data for category
        test_user_1 = User.objects.create_user(username='test_user_1', password='12345678')  # creating new user
        test_post = Post.objects.create(
            category_id=1, title='Post title', excerpt='Post Except', content='Post Content',
            slug='post-title', author_id=1, status='published'
        )  # creating post for foreignkey we use "_id" because takes an id
        """
        Now we can test the data
        """

    def test_blog_content(self):
        post = Post.post_objects.get(id=1)
        cat = Category.objects.get(id=1)
        author = f'{post.author}'
        excerpt = f'{post.excerpt}'
        title = f'{post.title}'
        content = f'{post.content}'
        status = f'{post.status}'
        self.assertEqual(author, 'test_user_1')
        self.assertEqual(title, 'Post title')
        self.assertEqual(content, 'Post Content')
        self.assertEqual(status, 'published')
        """
        Now we have to test our str methods that we have created and that what coverage tell us what have
        to test
        """
        self.assertEqual(str(post), 'Post title')  # we are testing str method post that have to match with title
        self.assertEqual(str(cat), 'django')  # we are testing str method cat that have to match with the name


