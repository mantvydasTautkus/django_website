from smith.forms import SnippetForm
from typing import Text
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Comment, GaleryItem, Product, GaleryItem, ProductImages, GaleryImages
from django.core.paginator import Paginator
from django.utils.translation import activate, get_language, gettext as _
from django.views.generic.edit import CreateView
from .forms import SnippetForm




def all_items(request, ):
    item_list = Product.objects.all()
    Item_paginator = Paginator(item_list, 5)
    page_num = request.GET.get("page")
    page = Item_paginator.get_page(page_num)

    context = {
        "count" : Item_paginator.count,
        "page" : page,
    }
    return render(request, 'base.html', context)

def galery(request):
    galery_list = GaleryItem.objects.all()
    galery_paginator = Paginator(galery_list, 5)
    page_num = request.GET.get("page")
    page = galery_paginator.get_page(page_num)

    context = {
        "count": galery_paginator.count,
        "galery_items": page,
    }
    return render(request, 'galery.html', context)


def subscribe(request):
    return render(request, 'subscribe.html')


def galery_item_view(request, galery_item_id):
    post = get_object_or_404(GaleryItem, id=galery_item_id)
    photos = GaleryImages.objects.filter(GaleryItem=post)
    return render(request, 'galery_item.html', context={
        'post':post,
        'photos':photos,
    })


def product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product_img = ProductImages.objects.filter(product=product)
    return render(request, "product.html", context={
        'product': product ,
        "product_img": product_img,
        })


def abaut_us(request):
    return render(request, "abaut_us.html")



def add_comment(request):

    if request.method == "POST":
        form = SnippetForm(request.POST)
        form.save()


    form = SnippetForm()
    return render(request,"add_comment.html", {"form": form})