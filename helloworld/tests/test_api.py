import json
from django.core.urlresolvers import reverse
from helloworld.tests.utils import LoggedInTestCase
from helloworld.models import UserInfo


class UserInfoApiTests(LoggedInTestCase):
    """
    Tests for the ProctoredExamView
    """
    def setUp(self):
        super(UserInfoApiTests, self).setUp()
        # self.user.is_staff = True
        # self.user.save()
        # self.client.login_user(self.user)

    def test_to_get_the_users_info_list(self):
        """
        Test to get the users info
        list.
        """
        for i in range(8):
            UserInfo.objects.create(name='{name}-{id}'.format(name='test_user', id=i))

        response = self.client.get(
            reverse('helloworld.users_info'),
        )

        self.assertEqual(response.status_code, 200)
        response_data = json.loads(response.content)

        self.assertEqual(len(response_data), 8)
        for i in range(8):
            self.assertEqual(response_data[i]['name'], '{name}-{id}'.format(name='test_user', id=i))
