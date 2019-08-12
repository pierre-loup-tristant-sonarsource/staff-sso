from django.contrib.auth.models import Group
from rest_framework import serializers

from .models import User


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('name',)


class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)

    class Meta:
        model = User

    def to_representation(self, obj):
        app = self.context['request'].auth.application

        primary_email, related_emails = obj.get_emails_for_application(app)

        return {
            'email': primary_email,
            'user_id': str(obj.user_id),
            'first_name': obj.first_name,
            'last_name': obj.last_name,
            'related_emails': related_emails,
            'groups': [],
            'permitted_applications': obj.get_permitted_applications(),
            'access_profiles': [profile.slug for profile in obj.access_profiles.all()]
        }


class UserParamSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False, default=None)
    user_id = serializers.UUIDField(required=False, default=None)

    def validate(self, data):
        if not data['email'] and not data['user_id']:
            raise serializers.ValidationError('Either an email or a user_id is required')

        return data


class UserDetailsSerializer(serializers.Serializer):
    contact_email = serializers.EmailField(required=False, default=None)
    first_name = serializers.CharField(required=False, default=None)
    last_name = serializers.CharField(required=False, default=None)

    def validate(self, data):
        if not data['contact_email'] and not data['first_name'] and not data['last_name']:
            raise serializers.ValidationError('Either a contact_email, first_name or last_name is required')

        return data

class UserListSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = (
            'user_id',
            'first_name',
            'last_name',
            'email',
        )

    def to_representation(self, obj):
        app = self.context['request'].auth.application

        primary_email, _ = obj.get_emails_for_application(app)

        return {
            'user_id': str(obj.user_id),
            'first_name': obj.first_name,
            'last_name': obj.last_name,
            'email': primary_email,
        }
