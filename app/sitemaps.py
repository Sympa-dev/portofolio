from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class SinglePageSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 1.0

    def items(self):
        return ['index']  # correspond au name='index'

    def location(self, item):
        return reverse(item)
