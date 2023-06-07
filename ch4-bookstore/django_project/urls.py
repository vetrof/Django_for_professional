
from django.contrib import admin
from django.urls import path, include

from pages.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls'))
]
