from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# Import views 
from App_store.views import Home

urlpatterns = [
    path('', Home, name ='home' ),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)