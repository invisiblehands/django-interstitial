from datetime import datetime

from django.db import models
from django.conf import settings
from django.core.cache import get_cache


class InterstitialManager(models.Manager):
    def get_interstitial(self):
        caching = getattr(settings, 'INTERSTITIAL_CACHE', True)
        if caching:
            cache = get_cache('default')
            interstitial = cache.get('interstitial')
            if interstitial:
                return interstitial

        today = datetime.now()
        interstitial = self.filter(active = True).first()

        if interstitial:
            if interstitial.start and interstitial.start > today:
                interstitial = None
            if interstitial.end and interstitial.end <= today:
                interstitial = None

        if caching:
            cache.set('interstitial', interstitial, 60 * 60)

        return interstitial


    def get_for_user(self, user):
        interstitial = self.get_interstitial()

        if interstitial and interstitial.draft:
            if user.is_staff():
                return interstitial

        return interstitial
