from django.urls import path
from .views import HomePageView, ProductDetailView, ProductDeleteView, ProductCreateView, ProductUpdateView
from .views import MyProductsView, CategoryView, LikedView, AddLikeView, ActivView
urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('my_products/', MyProductsView.as_view(), name='my-products'),
    path('detail/<int:product_id>/', ProductDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete'),
    path('new/', ProductCreateView.as_view(), name='new'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update'),
    path('liked/', LikedView.as_view(), name='liked'),
    path('add_like/<int:id>/', AddLikeView.as_view(), name='add-like'),
    path('activ/<int:id>/', ActivView.as_view(), name='activ'),
    path('category/<int:category_id>/', CategoryView.as_view(), name='category'),
]
