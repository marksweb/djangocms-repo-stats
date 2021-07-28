from django.contrib.auth.models import User

from cms.test_utils.testcases import CMSTestCase


class MockRequest:
    GET = {}


class BaseTestCase(CMSTestCase):
    @classmethod
    def setUpTestData(cls):
        # create user
        cls.user = User.objects.create_superuser(
            username="test", email="test@test.com", password="test"
        )


class BaseViewTestCase(BaseTestCase):
    def setUp(self):
        self.client.force_login(self.user)
