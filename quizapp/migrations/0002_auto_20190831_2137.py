# Generated by Django 2.2.3 on 2019-08-31 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='corr_answer',
            field=models.CharField(choices=[('1', 'Crocodile'), ('1', 'SP'), ('1', 'Bottle'), ('1', 'Oil')], max_length=1),
        ),
    ]
