# Generated by Django 4.1.2 on 2023-03-24 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scales_apiary', '0006_alter_weather_3_air_humidity_api_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather_3',
            name='wind_direction_ico_url',
            field=models.CharField(blank=True, max_length=2),
        ),
    ]
