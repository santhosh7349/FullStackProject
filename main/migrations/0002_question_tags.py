# Generated by Django 3.2 on 2022-04-13 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='tags',
            field=models.TextField(default=''),
        ),
    ]
