from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
# Import views 
from App_store.views import Home, ProductDetails
app_name="App_store"
urlpatterns = [
    path('', Home, name ='home' ),
    path('Product-Details/<str:slug>/', ProductDetails, name ='Product_Details' ),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)