# bookstore_project/urls.py
from django.conf import settings # new
from django.conf.urls.static import static # new
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
# Django admin
path('jet_api/', include('jet_django.urls')),
path("admin/", admin.site.urls),
# User management
path("accounts/", include("allauth.urls")),
# Local apps
path("", include("books.urls")),


] + static(
settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
) # new
