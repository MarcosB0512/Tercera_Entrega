# Generated by Django 3.2 on 2023-06-08 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0002_auto_20230608_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='fecha_update',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
