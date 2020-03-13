from rest_framework import serializers

from .models import Friend, Belonging, Borrowed

class FriendSerializer(serializers.ModelSerializer):
    model = Friend
    fields = ('id', 'name')

class BelongingSerializer(serializers.ModelSerializer):
    model = Belonging
    fields = ('id', 'name')

class BorrowedSerializer(serializers.ModelSerializer):
    model = Borrowed
    fields = ('id', 'what', 'who', 'when', 'returned')