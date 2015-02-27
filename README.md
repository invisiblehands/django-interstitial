# django-interstitial

### Just a simple django app for interstitials.

An arts and culture magazine likes to feature interstitial advertisements every once in a while directing users to links on and off the site.  This simply allows site editors to configure the interstitials.  It contains very basic jquery and css.  Still seems to look good :)

### Requirements

- django >= 1.5
- jquery

### Settings

- INTERSTITIAL_ON (default True)
- INTERSTITIAL_CACHE (default False)
- INTERSTITIAL_FORCE (default False)

### Install

1. Add to INSTALLED_APPS and syncdb.
2. Load tags {% interstitial_tags %}.
3. Make sure you're using the request context_processor.
4. At the bottom of the page {% get_interstitial request %}

### Notes

This assumes you're using html5.  If not, you might want to edit the interstitial.html and move the css and js to the head.
