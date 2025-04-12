from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('anon/email/',views.anon_email),
]