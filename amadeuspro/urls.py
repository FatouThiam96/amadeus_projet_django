from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hotel.urls')),
    path('inscription/', include('inscription.urls')),
    path('vols/', include('vols.urls')),
    path('hotel/', include('my_hotel.urls')),
    path('', include('espaceClient.urls')),
]   

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
