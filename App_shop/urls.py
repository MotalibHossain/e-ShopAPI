
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from App_shop.models import Articel, BlogCategory

# import views 
from App_shop.views import Home, productView, ProductDetailsView, ProductUpdate, CategoryUpdate, BlogArticel, BlogCategorys

urlpatterns = [
    path("", Home, name="home"),
    path("category-update/<int:pk>", CategoryUpdate, name="CategoryUpdate"),
    path("product/", productView, name="productView"),
    path("product-update/<int:pk>", ProductUpdate, name="ProductUpdate"),
    path("details/<int:pk>", ProductDetailsView, name="ProductDetailsView"),

    # ============================Blog post urls============================
    path("blog-category/", BlogCategorys, name="BlogCategorys"),
    path("blogs/", BlogArticel, name="BlogArticel"),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
