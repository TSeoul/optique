from . import views

from django.urls import path


urlpatterns = [
    path("", views.home, name="home"),
    path("contact.html", views.contact, name="contact"),
    path("about.html", views.about, name="about"),
    path("glasses.html", views.glasses, name="glasses"),
    path("shop.html", views.shop, name="shop"),


]
