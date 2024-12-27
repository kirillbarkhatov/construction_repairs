from rest_framework import generics

from .models import Worker
from .serializers import WorkerSerializer


class WorkerRetrieveAPIView(generics.RetrieveAPIView):
    """Получить информацию о работнике"""

    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()


class WorkersTeamListApiView(generics.ListAPIView):
    """Список работников бригады"""

    serializer_class = WorkerSerializer

    def get_queryset(self):
        """Фильтруем набор данных в зависимости от выбранной бригады"""

        team_id = self.kwargs.get("team_id")
        return Worker.objects.filter(team=team_id)
