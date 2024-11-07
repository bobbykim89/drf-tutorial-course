from django.urls import path
from . import views

urlpatterns = [
    path('', view=views.product_mixin_view),
    path('<int:pk>/update/', view=views.product_update_view),
    path('<int:pk>/delete/', view=views.product_delete_view),
    path('<int:pk>/', view=views.product_mixin_view)
]
