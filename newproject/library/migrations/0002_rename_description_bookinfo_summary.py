# Generated by Django 5.0.1 on 2024-01-11 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinfo',
            old_name='description',
            new_name='summary',
        ),
    ]
