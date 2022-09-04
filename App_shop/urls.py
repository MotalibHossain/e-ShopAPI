
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

# import views 
from App_shop.views import Home, productView, ProductDetailsView

urlpatterns = [
    path("", Home, name="home"),
    path("product/", productView, name="productView"),
    path("details/<int:pk>", ProductDetailsView, name="ProductDetailsView"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
