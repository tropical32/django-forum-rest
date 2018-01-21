import datetime
import json
from unittest import TestCase

from django.contrib.auth.models import User
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient

from forumapp.models import Forum, Thread, ForumSection, ForumUser


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

        user = User.objects.create_user(
            username='testuser',
            password='zaq12wrx'
        )

        forum_user = ForumUser.objects.create(
            user=user
        )

    def test_forum_get(self):
        client = APIClient()
        response = client.get(reverse('forum-list'))
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

    def test_create_thread_unauth(self):
        client = APIClient()
        response = client.post(
            reverse('thread-list'), {
                'name': 'thread1',
                'forum': 1,
                'pinned': True,
            }
        )

        # user not logged-in
        self.assertEquals(response.status_code, 401)

    def test_create_thread_auth_token(self):
        client = APIClient()
        response = client.post(
            '/forumapp/api-token-auth/',
            {
                'username': 'testuser',
                'password': 'zaq12wrx'
            }
        )
        token = response.data['token']

        response_thread = client.post(
            reverse('thread-list'),
            {
                'name': 'threadname',
                'forum': 1,
                'message': 'message1',
            },
            HTTP_AUTHORIZATION=f'JWT {token}'
        )

        self.assertEquals(json.loads(response_thread.content), {
            'name': 'threadname',
            'forum': 1,
            'pinned': False,
            'message': 'message1',
        })

    def test_create_thread_auth_token_while_banned(self):
        forum_user = ForumUser.objects.get(id=1)
        forum_user.banned_until += datetime.timedelta(days=30)

        client = APIClient()
        response = client.post(
            '/forumapp/api-token-auth/',
            {
                'username': 'testuser',
                'password': 'zaq12wrx'
            }
        )
        token = response.data['token']

        response_thread = client.post(
            reverse('thread-list'),
            {
                'name': 'threadname',
                'forum': 1,
                'message': 'message1',
            },
            HTTP_AUTHORIZATION=f'JWT {token}'
        )

        self.assertEquals(response_thread.status_code, 403)
