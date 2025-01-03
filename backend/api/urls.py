from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from . import views

urlpatterns = [
    path('auth/', view=obtain_auth_token),
    path('token/', view=TokenObtainPairView.as_view(),
         name='token_obtain_pair'),  # /api/token/
    path('token/refresh/', view=TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', view=TokenVerifyView.as_view(), name='token_verify'),
    path('', view=views.api_home),

]
