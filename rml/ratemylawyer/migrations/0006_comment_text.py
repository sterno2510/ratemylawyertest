# Generated by Django 4.0 on 2021-12-15 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratemylawyer', '0005_remove_comment_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default=True),
            preserve_default=False,
        ),
    ]
