from django.db import models


class Worker(models.Model):
    """Модель работников"""

    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    team = models.PositiveIntegerField(verbose_name="Номер бригады")
    salary = models.PositiveIntegerField(verbose_name="Зарплата")
    specialization = models.CharField(max_length=50, verbose_name="Специализация")

    def __str__(self):
        return f"{self.full_name} - Бригада № {self.team} - {self.specialization}"

    class Meta:
        verbose_name = "Работник"
        verbose_name_plural = "Работники"
        ordering = [
            "pk",
        ]
