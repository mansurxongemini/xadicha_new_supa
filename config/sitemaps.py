from django.contrib import sitemaps
from django.urls import reverse
from core.models import NewsBlog

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'
    protocol = 'https'

    def get_domain(self, site=None):
        return 'xadichasulaymonova.up.railway.app'

    def items(self):
        # 'home' bu core/urls.py ichidagi asosiy sahifaning nomi bo'lishi kerak.
        # Agar sizda boshqa sahifalar bo'lsa, ularni ham shu yerga qo'shishingiz mumkin.
        return ['home', 'biography', 'books', 'articles', 'videos', 'about', 'blog_list']

    def location(self, item):
        return reverse(item)

class BlogSitemap(sitemaps.Sitemap):
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        # objects.all() ni faqat items() ichida ishlating
        return NewsBlog.objects.all()