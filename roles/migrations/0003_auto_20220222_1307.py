# Generated by Django 3.2.9 on 2022-02-22 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roles', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.AddField(
            model_name='student',
            name='first_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='middle_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]