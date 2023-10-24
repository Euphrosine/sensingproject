# Generated by Django 4.2.6 on 2023-10-20 10:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(default=django.utils.timezone.now)),
                ('activity', models.CharField(max_length=100)),
                ('status', models.IntegerField(default=0)),
            ],
        ),
    ]