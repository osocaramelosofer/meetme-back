from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User


class BlogTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create a user instance
        testuser1 = User.objects.create_user(username='testuser1', password='abc123')
        testuser1.save()

        # Create a blog post
        test_post = Post.objects.create(author=testuser1, title='title', body='nice body')
        test_post.save()


    def test_blog_content(self):
        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author,'testuser1')
        self.assertEqual(title, 'title')
        self.assertEqual(body, 'nice body')

