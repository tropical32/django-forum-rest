import json
from unittest import TestCase

from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient

from forumapp.models import Forum, Thread, ForumSection


class ForumSectionModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        section = ForumSection.objects.create(name='section1')

        Forum.objects.create(
            name='Forum1',
            description='Desc1',
            section=section
        )
        Forum.objects.create(
            name='Forum2',
            description='Desc2',
            section=section
        )

    def test_forum_get(self):
        client = APIClient()
        response = client.get('/forumapp/rest/forums/')
        self.assertEqual(json.loads(response.content), [
            {
                'name': 'Forum1',
                'description': 'Desc1',
                'section': 1
            },
            {
                'name': 'Forum2',
                'description': 'Desc2',
                'section': 1
            }
        ])

    def test_create_thread(self):
        client = APIClient()
        response = client.post(
            '/forumapp/rest/threads/', {
                'name': 'thread1',
                'forum': 1,
                'pinned': True,
            }
        )

        # user not logged-in
        self.assertEquals(response.status_code, 403)
