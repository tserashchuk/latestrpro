from django.contrib.sitemaps import Sitemap
from recycle.models import Category, Article, Region, Product
from django.shortcuts import reverse

class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = "0.8"
    protocol = "https"
    
    def items(self):
        return Product.objects.all().order_by('product_slug')
        
    def lastmod(self, item):
        return item.pub_date

class CategorySitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7
    protocol = "https"

    def items(self):
        return Category.objects.all().order_by('cat_slug')

    def lastmod(self, item):
        return item.pub_date

class ServicesSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7
    protocol = "https"
    
    def items(self):
        return ['contact','punkty','news','priem','yuriki','bezvozm','spisanie','vyvoz', 'category','vacancies']

    def location(self, item):
        return reverse(item)

class HomeSitemap(Sitemap):
    changefreq = "weekly"
    priority = 1
    protocol = "https"
    
    def items(self):
        return ['home']

    def location(self, item):
        return reverse(item)
        
    #def lastmod(self, item):
    #    return item.pub_date

class ArticlesSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.2
    protocol = "https"
    
    def items(self):
        return Article.objects.all().order_by('article_slug')

    def lastmod(self, item):
        return item.pub_date

class RegionSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.2
    protocol = "https"
    
    def items(self):
        return Region.objects.all().order_by('region_slug')

    def lastmod(self, item):
        return item.pub_date
