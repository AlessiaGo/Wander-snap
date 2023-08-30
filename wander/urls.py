from django.contrib import admin
from django.urls import include, path

import listings

urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('listings.urls')),
    path('admin/', admin.site.urls),
]
