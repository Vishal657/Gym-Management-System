# Generated by Django 3.0.3 on 2020-03-13 08:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GymWebapp', '0002_subscription_package'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workoutplan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dietplan', models.CharField(max_length=1000)),
                ('Exercise', models.CharField(max_length=1000)),
                ('Customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GymWebapp.Customer_Details')),
            ],
        ),
    ]
