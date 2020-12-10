# coding: utf-8

from rest_framework import serializers
from .models import User, Entry, Account
from drf_writable_nested.serializers import WritableNestedModelSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail')

class AccountSerializer(serializers.ModelSerializer):
    account = UserSerializer()
    class Meta:
        model = Account
        fields = "__all__"

class EntrySerializer(WritableNestedModelSerializer):
# class EntrySerializer(WritableNestedModelSerializer, serializers.ModelSerializer):
    employee = UserSerializer()
    reporter = AccountSerializer()
    class Meta:
        model = Entry
        fields = ('employee', 'score', 'comment', 'created_at', 'status', 'reporter')

    def update(self, instance, validated_data): 
            instance.score = validated_data.get('score', instance.score)
            instance.comment = validated_data.get('comment', instance.comment)
            instance.status = validated_data.get('status', instance.status)
            return instance