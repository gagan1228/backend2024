from django.urls import path
from . import views
from rest_framework import routers
router=routers.DefaultRouter()
router.register('address',views.CustomerAddress)
router.register('productrating',views.ProductRating)
urlpatterns = [
    #vendors
    path('vendors/',views.VendorList.as_view()),
    path('vendor/<int:pk>/',views.VendorList.as_view()),
    #products
    path('products/',views.ProductList.as_view()),
    path('product/<int:pk>/',views.ProductDetail.as_view()),
    #productcategory
    path('categories/',views.CategoryList.as_view()),
    path('category/<int:pk>/',views.CategoryDetail.as_view()),
    #customers
    path('customers/',views.CustomertList.as_view()),
    path('customer/<int:pk>/',views.CustomerDetail.as_view()),
    path('customer/login/',views.customer_login,name='customer_login'),
    path('customer/register/',views.customer_register,name='customer_register'),
    #orders
    path('orders/',views.OrderList.as_view()),
    path('order/<int:pk>',views.OrderDetail.as_view()),
    #cart
    path('addtocart/',views.addtocartfun,name='addtocartfun')
]
urlpatterns+=router.urls