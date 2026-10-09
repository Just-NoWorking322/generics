from django.urls import path
from .views import CategoryListCreateView , CategoryDetailView
# ProductView

urlpatterns = [
    path('category/', CategoryListCreateView.as_view(),name='category'),
    path('category/<int:pk>/', CategoryDetailView.as_view(),name='category-detail'),

    ## primary key - первичный ключ Id  
    # path('product/', ProductView.as_view(),name='product'),
]


