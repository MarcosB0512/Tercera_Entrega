# Generated by Django 3.2 on 2023-06-13 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0008_entregable_fecha_de_entrega'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entregable',
            name='fecha_de_Entrega',
        ),
    ]
