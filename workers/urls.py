from django.urls import path

from .apps import WorkersConfig
from .views import

app_name = WorkersConfig.name


urlpatterns = [
    path("/api/v1/team/<team_id>/WorkerLis", LessonListApiView.as_view(), name="team_workers_list"),
    path("/api/v1/worker/<worker_id>", LessonRetrieveAPIView.as_view(), name="worker_retrieve"),
    # path("lesson/create", LessonCreateApiView.as_view(), name="lesson_create"),
    # path("lesson/<int:pk>/update", LessonUpdateAPIView.as_view(), name="lesson_update"),
    # path(
    #     "lesson/<int:pk>/delete", LessonDestroyAPIView.as_view(), name="lesson_delete"
    # ),
    # path(
    #     "course/subscribe", CourseSubscriptionApiView.as_view(), name="course_subscribe"
    # ),
    # path("payment/", CoursePaymentCreateApiView.as_view(), name="payment"),
]

# urlpatterns += router.urls