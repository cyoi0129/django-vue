# coding: utf-8

from rest_framework import serializers
from .models import User, Entry, Account

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail')

class AccountSerializer(serializers.ModelSerializer):
    account = UserSerializer()
    class Meta:
        model = Account
        # fields = ('account')
        fields = "__all__"

class EntrySerializer(serializers.ModelSerializer):
    employee = UserSerializer()
    reporter = AccountSerializer()
    class Meta:
        model = Entry
        fields = ('employee', 'score', 'comment', 'created_at', 'status', 'reporter')