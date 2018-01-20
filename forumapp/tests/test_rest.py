import json
from unittest import TestCase

from rest_framework.test import APIRequestFactory, force_authenticate, APIClient

from forumapp.models import Forum


class ForumSectionModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass

    def test_forum_get(self):
        Forum.objects.create(name='Forum1', description='Desc1')
        Forum.objects.create(name='Forum2', description='Desc2')

        client = APIClient()
        response = client.get('/forumapp/rest/forums')
        self.assertEqual(json.loads(response.content), [
            {
                'name': 'Forum1',
                'description': 'Desc1',
                'section': None
            },
            {
                'name': 'Forum2',
                'description': 'Desc2',
                'section': None
            }
        ])
