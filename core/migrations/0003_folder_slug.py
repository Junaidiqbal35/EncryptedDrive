# Generated by Django 5.0 on 2023-12-25 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_owner_file_file_owner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='folder',
            name='slug',
            field=models.SlugField(default='2'),
            preserve_default=False,
        ),
    ]