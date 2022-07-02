from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('firstapp.urls')),
    path('', include('bookstore.urls')),
    path('account/', include('account.urls')),
]
