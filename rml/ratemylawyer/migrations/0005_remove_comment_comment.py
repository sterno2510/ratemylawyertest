# Generated by Django 4.0 on 2021-12-15 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ratemylawyer', '0004_comment_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='comment',
        ),
    ]
