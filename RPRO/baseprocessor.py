from recycle.models import *


def custom_proc(request):
    stock = False
    articles = Article.objects.all()
    for article in articles:
        if article.isStock == True:
            stock = True
    return {'stock': stock}
