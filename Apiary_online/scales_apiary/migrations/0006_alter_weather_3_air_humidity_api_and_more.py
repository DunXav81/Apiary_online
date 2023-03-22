# Generated by Django 4.1.2 on 2023-03-20 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scales_apiary', '0005_alter_bienenkonigin_1_beehive_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weather_3',
            name='air_humidity_api',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='weather_3',
            name='air_humidity_sensor',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='weather_3',
            name='air_temperature_api',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='weather_3',
            name='air_temperature_sensor',
            field=models.SmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='weather_3',
            name='atmospheric_pressure_api',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='weather_3',
            name='weather_description_api',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='weather_3',
            name='wind_direction_api',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='weather_3',
            name='wind_power_api',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
