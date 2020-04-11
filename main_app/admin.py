from django.contrib import admin
from .models import Jersey, Player, Sponsor, Championship, Photo, Photo_player, Photo_sponsor 

# Register your models here.
admin.site.register(Jersey)
admin.site.register(Player)
admin.site.register(Photo)
admin.site.register(Photo_player)
admin.site.register(Photo_sponsor)
admin.site.register(Sponsor)
admin.site.register(Championship)