from rest_framework import serializers
from .models import post, person, interaction
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta, datetime


class postSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields =('postID', 'title', 'politics', 'health', 'sports', 'tech', 'message', 'image', 'timestamp', 'expireDateTime',
        'status', 'personID', 'likeCount', 'dislikeCount', 'commentCount')
        read_only_fields = ('timestamp', 'expireDateTime', 'status',  'likeCount', 'dislikeCount', 'commentCount' )



class personSerializer(serializers.ModelSerializer):
    class Meta:
        model = person
        fields =('personID', 'personName')
        


class interactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = interaction
        fields =('responseID', 'postID', 'personID', 'response_type', 'comments', 'is_expireDateTime', 'is_status', 'is_response_type1', 'is_response_type2')
        read_only_fields = ('responseID',  'is_expireDateTime', 'is_status', 'is_response_type1', 'is_response_type2')











    