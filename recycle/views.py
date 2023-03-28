import json

from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from recycle.models import *
from bitrix24 import *
#from bx24_orm import *

from django.db.models import FloatField
from django.db.models.functions import Cast

class Home(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, 'index.html', {'products':products[0:4]})

    def post(self, request):
        try:
            products12 = request.POST['ppp']
            phone = request.POST['PHONE']
            name = request.POST['NAME']
            bx24 = Bitrix24('https://rpro.bitrix24.by/rest/92/saku8kz7khsln7as/')
            bx24.callMethod('crm.lead.add',
                            fields={
                                "TITLE": name,
                                "NAME": 'sdfsfd',
                                "STATUS_ID": "NEW",
                                "OPENED": "Y",
                                "ASSIGNED_BY_ID": 76,
                                "PHONE": [{"VALUE": phone, "VALUE_TYPE": "WORK"}],
                                "UF_CRM_1614585863220": products12
                            },
                            )
        except Exception as e:
            print(e)

        return render(request, 'index.html')


class ArticleView(View):
    def get(self, request, article_slug):
        article = Article.objects.get(article_slug=article_slug)
        return render(request, 'article.html', {'article': article})
        
class Opt(View):
    def get(self, request):
        return render(request, 'opt.html')

class Review(View):
    def get(self, request, tone):
        punkt = Punkt.objects.get(id=request.GET.get('id'))
        if tone == 'positive':
            punkt.punkt_positive = punkt.punkt_positive + 1
            punkt.save()
        if tone == 'negative':
            punkt.punkt_negative = punkt.punkt_negative + 1
            punkt.save()

        return render(request, 'review.html',{'tone':tone, 'punkt':punkt})

class CategoryView(View):
    def get(self, request):
        categorys = Category.objects.all()
        return render(request, 'categorys.html', {'categorys': categorys})


class Products(View):
    def get(self, request, cat_slug):
        category = Category.objects.get(cat_slug=cat_slug)
        products = Product.objects.annotate(price_as_float = Cast('product_price', output_field=FloatField())).filter(category=category).order_by('-price_as_float')
        if products[0].color == 'Штук':
            alter_title = f'За 10 деталей {products[0].product_desc} артикула вы получите {products[0].price_as_float * 10} BYN'
            flag = products[0].price_as_float * 10
        else:
            alter_title = f'За 100 грамм {products[0].product_desc} артикула вы получите {round(products[0].price_as_float / 10, 4)} BYN'
            flag = products[0].price_as_float / 10
        return render(request, 'products.html', {'category': category,'promo_product':alter_title,'flag':flag})


class Singleproduct(View):
    def get(self, request, product_slug):
        product = Product.objects.get(product_slug=product_slug)
        return render(request, 'product.html', {'product': product})


class ProductModalView(View):
    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        return render(request, 'product-modal.html', {'product': product})


class Contact(View):
    messageSent = False
    products = Product.objects.all()

    def get(self, request):
        return render(request, 'contact.html', {'products': self.products, 'messageSent':  self.messageSent})

    def post(self, request):
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        send_mail(
            f"{surname} {name}",
            message,
            email,
            ["dierbekibragimov@gmail.com  "]
        )
        messageSent = True
        return render(request, 'contact.html', {'products': self.products, 'messageSent': messageSent})


class Skupka(View):
    def get(self, request):
        categorys = Category.objects.all()
        regions = Region.objects.all()
        return render(request, 'skupka.html', {'categorys': categorys, 'regions': regions})


class Punkty(View):
    def get(self, request):
        regions = Region.objects.all()
        return render(request, 'punkty.html', {'regions': regions})


class News(View):
    def get(self, request):
        stock = False
        articles = Article.objects.all().order_by("-pub_date")
        paginator = Paginator(articles, 8)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        for article in articles:
            if article.isStock == True:
                stock = True
        return render(request, 'news.html', {'articles': articles, 'stock': stock, 'page_obj': page_obj})


class Bytov(View):
    def get(self, request):
        return render(request, 'priem.html')


class Vyvoz(View):
    def get(self, request):
        return render(request, 'vyvoz.html')


class Yuriki(View):
    def get(self, request):
        return render(request, 'yuriki.html')


class Bezvozmezdno(View):
    def get(self, request):
        return render(request, 'bezvozmezdno.html')


class RegionView(View):
    def get(self, request, region_slug):
        region = Region.objects.get(region_slug=region_slug)
        categorys = Category.objects.all()
        return render(request, 'regionpage.html', {'region': region, 'categorys': categorys})


class Spisanie(View):
    def get(self, request):
        return render(request, 'spisanie.html')


class Job(View):
    def get(self, request):
        return render(request, 'job.html')
        
class Catalizator(View):
    def get(self, request):
        return render(request, 'cataliz.html')

def handle_error404(request, exception):
    return render(request, "404.html", status=404)
# a.bobkov@rpro.by


class Search(View):
    def get(self, request):
        return render(request, 'search.html')

    def post(self, request):
        senddata = {}
        senddataart = {}
        data = json.loads(request.body)
        products = Product.objects.all()
        i = 0
        for product in products:
            if product.product_desc == str(data['searchquery']):
                senddataart[product.id] = [product.product_name, product.product_price, product.color,
                                           product.product_desc]
        for product in products:
            if product.product_desc == str(data['searchquery']):
                continue
            if i > 50:
                break
            if product.product_name.lower().find(str(data['searchquery']).lower()) != -1:
                senddata[product.id] = [product.product_name,
                                        product.product_price, product.color, product.product_desc]
                i += 1
        return HttpResponse(json.dumps([senddata, senddataart]), content_type="application/json")
