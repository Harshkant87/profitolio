# Generated by Django 5.0.3 on 2024-04-01 10:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profitolio', '0002_rename_address_record_address_of_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='address_of_user',
            new_name='address',
        ),
    ]
