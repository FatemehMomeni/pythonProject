from rest_framework import serializers
from .models import UserPersonality, Contacts, Private, PublicInfo, Public, ChannelInfo, Channel


class UserPersonalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPersonality
        fields = '__all__'


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = '__all__'


class PrivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Private
        fields = '__all__'


class PublicInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicInfo
        fields = '__all__'


class PublicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Public
        fields = '__all__'


class ChannelInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChannelInfo
        fields = '__all__'


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'
