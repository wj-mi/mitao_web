from django.urls import path

from . import views
from . import products_view


urlpatterns = [
    # ex: /mitao_star/
    path('', products_view.ProductsListView.as_view(), name='index'),
    # ex: /mitao_star/detail/
    path('detail/<str:p_id>/', products_view.ProductView.as_view(), name='detail'),
    path("get_user_orders/<str:user_id>/", views.get_user_orders),
    path("order_detail/<str:order_id>/", products_view.OrderView.as_view()),

]
