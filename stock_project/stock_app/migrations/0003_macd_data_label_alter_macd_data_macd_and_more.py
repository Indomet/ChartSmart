# Generated by Django 5.1.3 on 2024-11-20 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0002_macd_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='macd_data',
            name='label',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='macd_data',
            name='macd',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='macd_data',
            name='macd_histogram',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='macd_data',
            name='signal_line',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
