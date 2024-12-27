from django.urls import path

from .apps import WorkersConfig
from .views import WorkerRetrieveAPIView, WorkersTeamListApiView

app_name = WorkersConfig.name


urlpatterns = [
    path(
        "api/v1/team/<team_id>/WorkerList",
        WorkersTeamListApiView.as_view(),
        name="team_workers_list",
    ),
    path(
        "api/v1/worker/<int:pk>",
        WorkerRetrieveAPIView.as_view(),
        name="worker_retrieve",
    ),
]
