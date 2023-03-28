import codecs
import csv

from django.contrib import admin
from django.shortcuts import render, redirect
from django.urls import path
from django_editorjs_fields import EditorJsJSONField
from recycle.forms import CsvImportForm
from recycle.models import *

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'article_name')

admin.site.register(Category, admin.ModelAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Region, admin.ModelAdmin)
admin.site.register(Punkt, admin.ModelAdmin)
admin.site.register(Agent, admin.ModelAdmin)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields = ['product_name']

    change_list_template = "admin/products_changelist.html"

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            reader = csv.DictReader(codecs.iterdecode(csv_file, 'utf-8'))
            for row in reader:
                product = Product.objects.filter(product_desc=row['art']).update(product_price=row['price'])
                print(product)
            self.message_user(request, "Продукты импортированы")
            return redirect("..")
        if request.method == "GET":
            form = CsvImportForm()
            payload = {"form": form}
            return render(request, "admin/csv_form.html", payload)