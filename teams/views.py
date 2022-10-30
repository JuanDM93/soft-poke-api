from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from teams.models import Team
from teams.serializers import TeamSerializer


class TeamViewSet(ModelViewSet):
    """
    Trainer can only update and delete their own teams.
    """
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        if self.request.user.is_anonymous or self.request.user.is_staff:
            return Team.objects.all()
        trainer = self.request.user.trainer
        return Team.objects.filter(trainer=trainer)

    def perform_create(self, serializer):
        serializer.save(trainer=self.request.user.trainer)
