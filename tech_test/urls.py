from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Public-facing views
    path('world-cup/', include('world_cup.urls')),
    # API endpoints
    path('api/', include('world_cup.api_urls')),
]
