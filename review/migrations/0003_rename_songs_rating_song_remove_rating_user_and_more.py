# Generated by Django 4.2.1 on 2023-05-08 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0002_like_created_at_alter_like_unique_together_favorite_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rating',
            old_name='songs',
            new_name='song',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='user',
        ),
        migrations.RemoveField(
            model_name='rating',
            name='value',
        ),
        migrations.AddField(
            model_name='rating',
            name='likes',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
