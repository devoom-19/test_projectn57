from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from Main_app import settings
from common.views import home_page, about_page, author_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('about/', about_page),
    path('author/', author_page)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)