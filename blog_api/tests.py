from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from blog.models import Post, Category
from django.contrib.auth.models import User


# Create your tests here.
from users.models import NewUser


class PostTest(APITestCase):
    """
    First we have to check that can view the post
    To view the post we have to go to entry point of our api
    """

    def test_view_posts(self):
        """
        getting the url using reverse to find out what the url is of our blog api
        list create so we are using blog_api list create
        in url we are using app_name='blog_api'  and the we are look the name in the path
        name='list_create'

        """
        url = reverse('blog_api:list_create')  # /api/
        """
        Now we create response that the self.client represent browser then in get
        we are putting the url and formatting it  in json format
        that will check the response we have to get response "200" (Accepted)
        """
        response = self.client.get(url, format='json')  # using GET method
        """
        Now we are checking by getting status from response and checking if it equal to status 200
        """
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    """
    Now lets check if we can create a post
    """

    def test_create_post(self):
        self.test_category = Category.objects.create(name='django')
        self.test_user_1 = NewUser.objects.create_user(email='s@s.com', user_name='test_user_1',
                                                       password='12345678', first_name='Sammy')
        """
        we are not specified category because by default it take 1
        """
        """
        We have to login like a use after we setup the permission
        """
        self.client.login(email=self.test_user_1.email, password='12345678')
        data = {
            'title': 'new',
            'author': 1,
            'excerpt': 'new',
            'content': 'new'
        }
        url = reverse('blog_api:list_create')
        """
        Now we have to post a data to create a data and check if the status is 201(created)
        """
        response = self.client.post(url, data, fromat='json')  # Using POST method
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_post_update(self):
        """
        For to check the update we have to create two users to check every user can change
        his own post
        """
        client = APIClient()
        self.test_category = Category.objects.create(name='django')
        self.test_user_1 = NewUser.objects.create_user(email='s@s.com', first_name='aaas', user_name='test_user_1', password='12345678')
        self.test_user_2 = NewUser.objects.create_user(email='s1@s.com', first_name='ffsfs', user_name='test_user_2', password='12345678')
        client.login(email=self.test_user_1.email, password='12345678')

        """
        Creating the post that can be updated
        """
        test_post = Post.objects.create(
            category_id=1, title='Post title', excerpt='Post Excerpt',
            content='Post Content', slug='post-title', author_id=1, status='published'
        )
        """
        Taking the path of the endpoint detail_create an adding the pk for choosing a post
        of the user that he created
        """
        url = reverse('blog_api:detail_create', kwargs={'pk': 1})
        """
        Now we have to create the update response
        """
        response = client.put(
            url, {
                'id': 1,  # adding the id where we specify in url kwargs pk: 1 mean the post that we what to edit
                'title': "New",
                'author': 1,
                'excerpt': "New",
                'content': 'New',
                'status': 'published'
            }, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
