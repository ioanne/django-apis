# Generated by Django 4.2.5 on 2023-09-29 22:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('character', '0001_initial'),
        ('item', '0001_initial'),
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Inventary',
            new_name='Inventory',
        ),
    ]