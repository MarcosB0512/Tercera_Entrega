# Generated by Django 3.2 on 2023-06-08 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0003_alter_curso_fecha_update'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='camada',
            field=models.IntegerField(default=10000),
        ),
    ]