from smith.forms import SnippetForm
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse, request
from .models import Comment, Landing_photos, Product, GaleryItem, ProductImages, GaleryImages
from django.core.paginator import Paginator
from django.utils.translation import gettext
from .forms import SnippetForm
from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm, User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth import login, logout


def all_items(request, ):
    item_list = Product.objects.all()
    landing_photos = Landing_photos.objects.all()
    Item_paginator = Paginator(item_list, 6)
    page_num = request.GET.get("page")
    page = Item_paginator.get_page(page_num)

    context = {
        "count" : Item_paginator.count,
        "page" : page,
        "landing_photos" : landing_photos
    }
    return render(request, 'base.html', context)

def galery(request):
    galery_list = GaleryItem.objects.all()
    galery_paginator = Paginator(galery_list, 99)
    page_num = request.GET.get("page")
    page = galery_paginator.get_page(page_num)

    context = {
        "count": galery_paginator.count,
        "galery_items": page,
    }
    return render(request, 'galery.html', context)


def subscribe(request):
    return render(request, 'subscribe.html')


def galery_item(request, galery_item_id):
    galeryitem = get_object_or_404(GaleryItem, id=galery_item_id)
    photos = GaleryImages.objects.filter(galeryitem=galery_item_id)
    return render(request, 'galery_item.html', context={
        'galery_item': galeryitem,
        'photos' : photos,
    })


def product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product_img = ProductImages.objects.filter(product=product)
    return render(request, "product.html", context={
        'product': product ,
        "product_img": product_img,
        })


def abaut_us(request):
    comments = Comment.objects.all()
    return render(request, "abaut_us.html", {"comments": comments})



def add_comment(request):

    if request.method == "POST":
        form = SnippetForm(request.POST)
        form.save()
        return redirect("abaut_us")


    form = SnippetForm()
    return render(request,"add_comment.html", {"form": form})


@csrf_protect
def register(request):
    if request.method == "POST":
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(
                    request, gettext("User name"), {username}, gettext("taken"),"!")
                return redirect('register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(
                        request, gettext("User with @mail"), {email}, gettext("allready exists"),"!")
                    return redirect('register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    return render(request, "login.html")

        else:
            messages.error(request, gettext("Passwords do not mach"),"!")
            return redirect('register')
    return render(request, 'register.html')



def login_view (request):
    if request.method == "POST":
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            #log in
            user = form.get_user()
            login(request, user)
            return redirect("/")
    else:
        form = AuthenticationForm()

    return render(request, "login.html",{
        "form" : form
    })

    

def lgout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("/")


