# Generated by Django 3.0.3 on 2020-03-13 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GymWebapp', '0003_workoutplan'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subscription',
            name='payment',
            field=models.BigIntegerField(),
        ),
    ]
