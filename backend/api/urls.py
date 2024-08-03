from django.urls import path
from api import views

urlpatterns = [
    path('<int:pk>',views.ProductDetailApiView.as_view(),name='home'),
    path('create_product',views.ProductCreateApiView.as_view(),name="create"),
    path('list_view/',views.ProductListView.as_view()),
    path('update/<int:pk>',views.ProductUpdateView.as_view()),
    path('delete/<int:pk>',views.ProductDeleteView.as_view())
]
