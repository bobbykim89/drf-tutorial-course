from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('auth/', view=obtain_auth_token),
    path('', view=views.api_home)
]
