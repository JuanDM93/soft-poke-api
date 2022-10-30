from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.status import HTTP_201_CREATED
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny, IsAdminUser,
)

from trainers.models import Trainer
from trainers.serializers import (
    TrainerSerializer,
    TrainerSignUpSerializer,
)


class TrainerList(ListCreateAPIView):
    """
    List all trainers, or create a new trainer. Only for admin users
    """
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    permission_classes = (IsAdminUser,)


class TrainerDetail(RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a trainer instance. Only for admin users
    """
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    permission_classes = (IsAdminUser,)
    lookup_field = 'uuid'


class TrainerSignUp(CreateAPIView):
    """
    Trainer signup view. Anyone can create a trainer
    """
    serializer_class = TrainerSignUpSerializer
    permission_classes = (AllowAny,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        trainer = serializer.save()
        return Response(
            TrainerSerializer(trainer).data,
            status=HTTP_201_CREATED,
        )
