
from django.urls import path
from .import views
from ecommerceproject import settings
app_name='shop'
urlpatterns = [
    path('',views.allProductCat,name='allProductCat'),
    path('<slug:c_slug>/',views.allProductCat,name='product-by-category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.proDetail, name='prodCatDetail')
]