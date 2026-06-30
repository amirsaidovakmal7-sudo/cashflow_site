from django.contrib import admin

from . models import *

admin.site.register(Event)
admin.site.register(Team)
admin.site.register(BrandLogo)
admin.site.register(GamesCategory)
admin.site.register(Games)
admin.site.register(Game_photo)


