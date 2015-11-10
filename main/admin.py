# -*- encoding: utf-8 -*-

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from main.models import Picture

class PictureAdmin(admin.ModelAdmin):
    list_display = ["image_tag", 'active', "is_publish", "publish_date", "expiry_date"]

    def active(self, obj):
        return obj.is_active
    active.short_description = _(u"發佈中")

admin.site.register(Picture, PictureAdmin)
