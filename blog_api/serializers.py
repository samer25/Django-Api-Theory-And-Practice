from rest_framework import serializers
from blog.models import Post

"""
We serializer a data that can be sure that we return a data in right format to browser
that can be viewable to our application
serializer allows data such data from query sets for example and models to be converted
into python data types that can then be easily rendered into JSOM or different type of data
"""


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'slug', 'title', 'author', 'excerpt', 'content', 'status')
