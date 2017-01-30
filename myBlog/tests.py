from django.test import TestCase
from .models import Post


class PostTest(TestCase):
    """
    Here we'll define the tests that will run against our Post model
    """

    def test_str(self):
        test_title = Post(title='My Latest Blog Post')
        self.assertEqual(str(test_title),
                         'My Latest Blog Post')

# Create your tests here.
