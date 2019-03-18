from django.contrib import admin
from django.urls import path

from spaces.views import index_view, space_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view),
    path('space', space_view)
]
