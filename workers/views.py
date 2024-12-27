from rest_framework import generics

from .models import Worker
from .serializers import WorkerSerializer

class WorkerRetrieveAPIView(generics.RetrieveAPIView):
    """Получить информацию о работнике"""

    serializer_class = WorkerSerializer
    queryset = Worker.objects.all()
