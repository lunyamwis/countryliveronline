# Generated by Django 3.2.9 on 2022-02-22 13:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_member',
            new_name='is_business',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_minister',
            new_name='is_student',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_ministry',
            new_name='is_teacher',
        ),
    ]