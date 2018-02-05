from rest_framework import serializers

from forumapp.models import Forum, Thread, ForumUser, ThreadResponse, \
    LikeDislike, ForumSection


class ForumSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForumSection
        fields = '__all__'


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        # fields = ('name', 'forum', 'pinned', 'threadresponse_set')
        fields = (
            'name', 'forum', 'pinned', 'message',
            'creator', 'id', 'created_datetime', 'last_activity',
            'threadresponse_set'
        )
        # fields = '__all__'
        extra_kwargs = {
            'pinned': {'read_only': True},
            'id': {'read_only': True},
            'creator': {'read_only': True},
        }


class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = (
            'id',
            'name',
            'description',
            'section',
            'thread_set'
        )


class ThreadResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreadResponse
        fields = ('thread', 'message', 'created_datetime', 'id', 'creator')
        extra_kwargs = {
            'created_datetime': {'read_only': True},
            'id': {'read_only': True},
            'responder': {'read_only': True}
        }


class ForumUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')

    class Meta:
        model = ForumUser
        fields = ['banned_until', 'username', 'id']
        extra_kwargs = {
            'user': {'read_only': True},
            'username': {'read_only': True},
            'id': {'read_only': True},
        }


class LikeDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeDislike
        fields = ['like', 'response', ]
