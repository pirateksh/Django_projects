# Generated by Django 2.2.3 on 2019-09-01 12:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0007_auto_20190901_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='date_created',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
