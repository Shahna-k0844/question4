from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
class QuestionSerializer(serializers.ModelSerializer):
    id=serializers.IntegerField(read_only=True)
    class Meta:
        model=Question
        fields="__all__"
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Answer
        fields="__all__"
        read_only_fields=['question']
class UserSerializer(serializers.ModelSerializer) :
    class Meta:
        model=User   
        fields=['username','password']
    def create(self,data):
        user=User.objects.create(username=data['username'])
        user.set_password(data['password'])
        user.save()
        return data        