# Generated by Django 3.2.9 on 2021-11-13 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitness_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(default='SOME STRING'),
        ),
    ]
