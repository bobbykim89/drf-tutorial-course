from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.product_list_create_view, name='product-list'),
    path('<int:pk>/update/', view=views.product_update_view, name='product-edit'),
    path('<int:pk>/delete/', view=views.product_delete_view),
    path('<int:pk>/', view=views.product_detail_view, name='product-detail')
]
