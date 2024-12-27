from django.core.management.base import BaseCommand

from workers.models import Worker


class Command(BaseCommand):
    help = "Добавление тестовых данных"

    def handle(self, *args, **kwargs):

        # Удаляем существующие записи
        Worker.objects.all().delete()

        workers = [
            Worker(
                full_name="Иванов",
                team=1,
                salary=10000,
                specialization="Черновая отделка",
            ),
            Worker(
                full_name="Петров",
                team=2,
                salary=12000,
                specialization="Черновая отделка",
            ),
            Worker(
                full_name="Сидоров", team=1, salary=16000, specialization="Бригадир"
            ),
            Worker(full_name="Сергеев", team=1, salary=20000, specialization="Прораб"),
            Worker(full_name="Сергеев", team=2, salary=20000, specialization="Прораб"),
        ]

        Worker.objects.bulk_create(workers)

        self.stdout.write(
            self.style.SUCCESS("В базу добавлено 5 тестовых записей о работниках")
        )
