from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from Shopify import views


# All the url patterns used for front and back end
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.home, name='index'),
    url(r'.*getAllFruits/', views.getAllFruits),
    url(r'.*getList/', views.getList),
    url(r'.*purchase/', views.purchase),
]
