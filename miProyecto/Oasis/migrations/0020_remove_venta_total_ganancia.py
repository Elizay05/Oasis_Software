# Generated by Django 4.2.6 on 2024-10-16 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Oasis', '0019_mesa_pedidos'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='total_ganancia',
        ),
    ]
