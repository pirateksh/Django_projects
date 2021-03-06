# Generated by Django 2.1.5 on 2019-04-03 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead_allot', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leader',
            name='password',
            field=models.CharField(max_length=500, null=True, verbose_name='Hashed Password'),
        ),
        migrations.AddField(
            model_name='leader',
            name='rank',
            field=models.IntegerField(default=0, verbose_name='Rank'),
        ),
        migrations.AlterField(
            model_name='leader',
            name='reg_no',
            field=models.CharField(max_length=256, verbose_name='Registration Number'),
        ),
        migrations.AlterField(
            model_name='student',
            name='reg_no',
            field=models.CharField(max_length=256, verbose_name='Registration Number'),
        ),
    ]
