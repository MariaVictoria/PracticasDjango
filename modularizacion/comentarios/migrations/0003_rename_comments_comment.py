# Generated by Django 5.0.6 on 2024-07-14 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comentarios', '0002_delete_author_comments_date'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='comments',
            new_name='Comment',
        ),
    ]
