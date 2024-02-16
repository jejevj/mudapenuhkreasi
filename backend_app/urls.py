from django.urls import path
from backend_app.views import *
urlpatterns = [
    path('',home,name='home_backend')
]
