"""RPRO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps import views as sitemapViews
from django.urls import path, include
from django.views.generic.base import TemplateView

from recycle import views, rest
from recycle.sitemap import CategorySitemap, ArticlesSitemap, ServicesSitemap, RegionSitemap, HomeSitemap, ProductSitemap

# Sitemap
sitemaps = {
    'home': HomeSitemap,
    'product': ProductSitemap,
    'category': CategorySitemap,
    'article': ArticlesSitemap,
    'service': ServicesSitemap,
    'punkt': RegionSitemap,
}

# URLs
urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.Home.as_view(), name='home'),
    path('category', views.CategoryView.as_view(), name='category'),
    path('category/<str:cat_slug>', views.Products.as_view(), name='products'),
    path('product/<str:product_slug>', views.Singleproduct.as_view(), name='product'),
    path('product/modal/<int:product_id>', views.ProductModalView.as_view(), name='product-modal'),
    path('contact', views.Contact.as_view(), name='contact'),
    path('review/<str:tone>', views.Review.as_view(), name='review'),
    path('skupka-radiodetaley', views.Skupka.as_view(), name='skupka'),
    path('punkty-priema', views.Punkty.as_view(), name='punkty'),
    path('news', views.News.as_view(), name='news'),
    path('optovym-klientam', views.Opt.as_view(), name='opt'),
    path('news/<str:article_slug>', views.ArticleView.as_view(), name='article'),
    path('priem-bytovoy-tehniki', views.Bytov.as_view(), name='priem'),
    path('vyvos-bytovoy-tehniki', views.Vyvoz.as_view(), name='vyvoz'),
    path('utilizaciya-tehniki', views.Yuriki.as_view(), name='yuriki'),
    path('bezvozmezdnaya', views.Bezvozmezdno.as_view(), name='bezvozm'),
    path('skupka-katalizatorov', views.Catalizator.as_view(), name='catalizator'),
    path('spisanie-teh-sostoyanie', views.Spisanie.as_view(), name='spisanie'),
    path('vacancies', views.Job.as_view(), name='vacancies'),
    path('region/<str:region_slug>', views.RegionView.as_view(), name='region'),
    path('editorjs', include('django_editorjs_fields.urls')),
    path('api-auth/', include(rest.router.urls)),
    path('search', views.Search.as_view(), name='search'),
    path("robots.txt", TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
    path('sitemap.xml', sitemapViews.sitemap, {
        'sitemaps': sitemaps,
        'template_name': 'sitemap.html'
    })
]


# Custom Template for 404 error
handler404 = "recycle.views.handle_error404"

# For static and media files
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
