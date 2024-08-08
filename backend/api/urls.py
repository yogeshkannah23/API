from django.urls import path
from api import views

urlpatterns = [
    path('<int:pk>',views.ProductDetailApiView.as_view(),name='product-detail'),
    path('create_product',views.ProductCreateApiView.as_view(),name="product-create"),
    path('list_view/',views.ProductListView.as_view()),
    path('update/<int:pk>',views.ProductUpdateView.as_view(),name='product-edit'),
    path('delete/<int:pk>',views.ProductDeleteView.as_view()),
    path('mixin_list/',views.ProductMixinView.as_view())
]
