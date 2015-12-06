__author__ = 'diwakarmahajan'
from rest_framework import serializers
from poll.models import Poll

class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poll
        fields = ('id', 'created', 'user_name', 'poll_name', 'vote')