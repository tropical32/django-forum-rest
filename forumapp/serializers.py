from rest_framework import serializers

from forumapp.models import Forum, Thread


class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = ('name', 'description', 'section')


class ThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thread
        # fields = ('name', 'forum', 'pinned', 'threadresponse_set')
        fields = ('name', 'forum', 'pinned', 'message')
        # fields = '__all__'
        extra_kwargs = {
            'pinned': {'read_only': True}
        }
