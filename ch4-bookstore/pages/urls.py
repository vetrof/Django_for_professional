

from django.contrib import admin
from django.urls import path, include

from pages.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),

]
