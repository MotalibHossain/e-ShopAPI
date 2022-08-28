
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("App_store.urls")),
    path("", include("App_UserProfile.urls")),
    path("api/", include("App_shop.urls")),
]
