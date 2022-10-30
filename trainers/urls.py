from django.urls import path

from trainers.views import (
    TrainerList,
    TrainerDetail,
    TrainerSignUp,
)


urlpatterns = [
    path('', TrainerList.as_view(), name='trainer-list'),
    path('<uuid:uuid>', TrainerDetail.as_view(), name='trainer-detail'),

    path('signup', TrainerSignUp.as_view(), name='trainer-signup'),
]
