from django.contrib import admin

# Register your models here.

from .models import Bienenkonigin_1, Weight_2, Weather_3

admin.site.register(Bienenkonigin_1)
admin.site.register(Weight_2)
#admin.site.register(Weather_3)

@admin.register(Weather_3)
class WeatherAdmin(admin.ModelAdmin):
    date_hierarchy = 'date_time_fixing_values'
    list_display = ("id", "date_time_fixing_values", "air_temperature_api",
    "air_humidity_api", "atmospheric_pressure_api", "wind_power_api",
    "wind_gust_api", "wind_direction_api", "weather_description_api", "daytime_api")
    list_per_page = 20
    # list_max_show_all = 60
    # list_filter = ("date_time_fixing_values", "daytime_api")

'''
    fields = ('date_time_fixing_values', 'air_temperature_api')
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]
'''