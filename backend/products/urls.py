from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.product_list_create_view),
    path('<int:pk>/', view=views.product_detail_view)
]
