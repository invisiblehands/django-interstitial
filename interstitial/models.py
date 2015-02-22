from django.db import models
from interstitial.managers import InterstitialManager


class Interstitial(models.Model):
    objects = InterstitialManager()
    name = models.CharField('Name', max_length=200)
    link = models.URLField('URL', null=False, blank=False)
    image = models.ImageField('image', max_length=250, upload_to='uploads/interstitials/', null=False, blank=False)
    start = models.DateTimeField('start', null=True, blank=True)
    end = models.DateTimeField('end', null=True, blank=True, help_text='If empty this will require manual deactivation.')
    active = models.BooleanField('active', default=False)
    draft = models.BooleanField('draft', default=True, help_text='The interstitial will only be presented to staff users.')


    class Meta: 
        verbose_name = 'Interstitial'
        verbose_name_plural = 'Interstitial'


    def __unicode__(self):
        return '%s' % self.name


    def save(self, *args, **kwargs):
        if self.active:
            # only allow one at a time
            Interstitial.objects.update(active=False)

        super(Interstitial, self).save(*args, **kwargs)