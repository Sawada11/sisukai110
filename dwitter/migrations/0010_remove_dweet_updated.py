# Generated by Django 4.1.5 on 2023-01-08 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dwitter', '0009_rename_created_at_dweet_created_dweet_updated_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dweet',
            name='updated',
        ),
    ]