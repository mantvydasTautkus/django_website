from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='base.html'),
    path("subscribe/", views.subscribe, name='subscribe'),
    path("admin/", views.subscribe, name='admin'),
    path('accounts/', include('django.contrib.auth.urls')),
]
