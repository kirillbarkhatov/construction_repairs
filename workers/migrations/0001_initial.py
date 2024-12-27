# Generated by Django 5.1.4 on 2024-12-27 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200, verbose_name='ФИО')),
                ('team', models.PositiveIntegerField(verbose_name='Номер бригады')),
                ('salary', models.PositiveIntegerField(verbose_name='Зарплата')),
                ('specialization', models.CharField(max_length=50, verbose_name='Специализация')),
            ],
            options={
                'verbose_name': 'Работник',
                'verbose_name_plural': 'Работники',
                'ordering': ['pk'],
            },
        ),
    ]
