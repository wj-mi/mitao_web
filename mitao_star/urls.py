from django.urls import path

from . import views
from . import products_view


urlpatterns = [
    # ex: /polls/
    path('', products_view.ProductsView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
