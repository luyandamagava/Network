# Generated by Django 4.1.7 on 2023-08-07 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0004_alter_user_followers_alter_user_following'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='following',
            new_name='user_followers',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='followers',
            new_name='user_following',
        ),
    ]
