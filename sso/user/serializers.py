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


class EmailParamSerializer(serializers.Serializer):
    email = serializers.EmailField()
