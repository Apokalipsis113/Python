from django.contrib import admin
from .models import Genge, Movie
# Register your models here.


class GengeAdmin(admin.ModelAdmin):
    list_display = ('name', 'id')


class MovieAdmin(admin.ModelAdmin):
    exclude = ('date_created',)
    list_display = ('title', 'number_in_stock', 'daily_rate')


admin.site.register(Genge, GengeAdmin)
admin.site.register(Movie, MovieAdmin)
