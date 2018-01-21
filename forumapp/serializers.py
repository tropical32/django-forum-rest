from rest_framework import serializers

from forumapp.models import Forum, Thread, ForumUser, ThreadResponse, \
    LikeDislike


class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = ('name', 'description', 'section', 'thread_set')


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        # fields = ('name', 'forum', 'pinned', 'threadresponse_set')
        fields = ('name', 'forum', 'pinned', 'message', 'creator')
        # fields = '__all__'
        extra_kwargs = {
            'pinned': {'read_only': True}
        }


class ThreadResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThreadResponse
        fields = ('thread', 'message', 'created_datetime')
        extra_kwargs = {
            'created_datetime': {'read_only': True}
        }


class ForumUserSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(source='user.username')

    class Meta:
        model = ForumUser
        fields = ['user', 'banned_until']
        extra_kwargs = {
            'user': {'read_only': True},
            # 'username': {'read_only': True},
        }


class LikeDislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeDislike
        fields = ['like', 'response', ]
