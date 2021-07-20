from django.urls import path, include
from . import views
from mysite import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('', views.all_items, name='base'),
    path('<int:product_id>', views.product, name='product'),
    path("subscribe/", views.subscribe, name='subscribe'),
    path("admin/", views.subscribe, name='admin'),
    path("galery/", views.galery, name="galery"),
    path("galery/<int:galery_item_id>", views.galery_item_view, name="galery_item"),
    path("abaut_us/", views.abaut_us, name="abaut_us"),
    path("snippet/", views.add_comment, name="add_comment"),
    path('i18n/', include('django.conf.urls.i18n')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
