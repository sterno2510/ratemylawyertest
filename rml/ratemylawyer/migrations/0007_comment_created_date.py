# Generated by Django 4.0 on 2021-12-15 19:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ratemylawyer', '0006_comment_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]