# Generated by Django 5.1 on 2024-11-25 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0002_rsimodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='RSIModel',
            new_name='RSI_Data',
        ),
    ]
