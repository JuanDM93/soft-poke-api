from rest_framework import serializers

from teams.models import Team

from trainers.serializers import TrainerSerializer


class TeamSerializer(serializers.ModelSerializer):

    uuid = serializers.UUIDField(read_only=True, required=False)
    owner = TrainerSerializer(read_only=True, required=False)

    class Meta:
        model = Team
        fields = [
            'uuid',
            'name',
            'owner',
        ]
