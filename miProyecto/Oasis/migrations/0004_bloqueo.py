# Generated by Django 4.2.7 on 2024-09-03 01:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Oasis', '0003_alter_mesa_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bloqueo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('motivo', models.TextField()),
                ('fecha_bloqueo', models.DateTimeField(auto_now_add=True)),
                ('realizado_por', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bloqueos_realizados', to=settings.AUTH_USER_MODEL)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bloqueos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
