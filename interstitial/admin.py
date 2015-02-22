from django import forms
from django.contrib import admin

from interstitial.models import Interstitial


class InterstitialAdmin(admin.ModelAdmin):
    list_display = ('name', 'link', 'start', 'end', 'active',)


admin.site.register(Interstitial, InterstitialAdmin)