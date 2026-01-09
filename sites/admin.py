from django.contrib import admin
from .models import (
    Site,
    Olympiade,
    Typologie,
    Denomination,
    DateReference
)


@admin.register(Site)
class SiteAdmin(admin.ModelAdmin):
    list_display = ("nom", "commune", "departement", "site_olympique")
    list_filter = ("departement", "site_olympique", "typologies")
    search_fields = ("nom", "commune", "description")
    filter_horizontal = ("typologies", "denominations", "dates_reference")


admin.site.register(Olympiade)
admin.site.register(Typologie)
admin.site.register(Denomination)
admin.site.register(DateReference)
