from django.core.urlresolvers import reverse
from django.test.client import Client
from django.test import TestCase
from helloworld.models import UserInfo


class TestViews(TestCase):
    """
    All tests for the views.py
    """

    def setUp(self):
        """
        Setup for tests
        """

        self.client = Client()

    def test_home_page(self):
        """
        test to check that the home page render
        successfully
        """
        response = self.client.get(reverse('helloworld.views.home'))
        self.assertIn('<input type="submit" value="Add" />', response.content)

    def test_add_user_info(self):
        """
        Test to verify the post request
        add the use info in the database table.
        """
        name = 'test_user'
        response = self.client.post(reverse('helloworld.views.home'), {'name': name})

        user_info = UserInfo.objects.filter(name=name)
        self.assertEqual(len(user_info), 1)
        self.assertIn(name, response.content)