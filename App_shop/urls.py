
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

# import views 
from App_shop.views import Home

urlpatterns = [
    path("", Home.as_view(), name="home"),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
