from rest_framework.serializers import (
    ModelSerializer,
    Serializer,
    SerializerMethodField,
    CharField,
    ValidationError,
)

from django.contrib.auth import get_user_model
from django.db import IntegrityError

from trainers.models import Trainer


class TrainerSerializer(ModelSerializer):

    username = SerializerMethodField()

    class Meta:
        model = Trainer
        fields = [
            'uuid',
            'username',
        ]

    def get_username(self, obj):
        return obj.user.username


class TrainerSignUpSerializer(Serializer):

    username = CharField(max_length=100, required=True)
    password = CharField(max_length=100, required=True)

    def validate(self, attrs):
        try:
            user = get_user_model().objects.create_user(
                username=attrs['username'],
                password=attrs['password'],
            )
        except IntegrityError as e:
            raise ValidationError("Username already exists")
        attrs['user'] = user
        return attrs

    def create(self, validated_data):
        user = validated_data.pop('user')
        return Trainer.objects.create(user=user)
