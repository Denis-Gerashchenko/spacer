from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from spaces.views import index_view, space_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view),
    path('space', space_view)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)