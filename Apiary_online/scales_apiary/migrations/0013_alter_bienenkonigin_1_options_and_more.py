# Generated by Django 4.1.2 on 2023-03-31 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scales_apiary', '0012_weather_3_daytime_api'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bienenkonigin_1',
            options={'ordering': ['beehive_number']},
        ),
        migrations.AlterModelOptions(
            name='weather_3',
            options={'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='weight_2',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='weather_3',
            name='date_time_fixing_values',
            field=models.DateTimeField(verbose_name='Дата/Время'),
        ),
    ]
