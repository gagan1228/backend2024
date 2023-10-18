from rest_framework import generics,permissions,pagination,viewsets
from . import serializers
from . import models
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError


# Create your views here.

class VendorList(generics.ListCreateAPIView):#Responsible for listing and adding the data
    queryset = models.Vendor.objects.all()
    serializer_class=serializers.VendorSerializer
    


class VendorDetail(generics.RetrieveUpdateDestroyAPIView):#responsible for fetching single data destroying the single data updating single data
    queryset = models.Vendor.objects.all()
    serializer_class=serializers.VendorDetailSerializer


class ProductList(generics.ListCreateAPIView):#Responsible for listing and adding the data
    queryset = models.Product.objects.all()
    serializer_class=serializers.ProductListSerializer
    pagination_class=pagination.PageNumberPagination


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):#responsible for fetching single data destroying the single data updating single data
    queryset = models.Product.objects.all()
    serializer_class=serializers.ProductDetailSerializer


class CustomertList(generics.ListCreateAPIView):#Responsible for listing and adding the data
    queryset = models.CustomerModel.objects.all()
    serializer_class=serializers.CustomerSerializer


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):#responsible for fetching single data destroying the single data updating single data
    queryset = models.CustomerModel.objects.all()
    serializer_class=serializers.CustomerDetailSerializer

@csrf_exempt
def customer_login (request):
    username=request.POST.get('username')
    password=request.POST.get('password')
    user=authenticate(username=username,password=password)
    if user:
        msg={
            'bool':True,
            'user':user.username,
            'id':user.id,
            'msg':"Thank you for the registration please login"
        }
    else:
        msg={
            'bool':False,
            'user':"Invalid user name or password"
        }
    return JsonResponse(msg)


@csrf_exempt
def customer_register (request):
    first_name=request.POST.get('first_name')
    last_name=request.POST.get('last_name')
    email=request.POST.get('email')
    username=request.POST.get('username')
    password=request.POST.get('password')
    phone=request.POST.get('phone')
    try:
        user=User.objects.create(first_name=first_name,
                                last_name=last_name,
                                email=email,
                                username=username,
                                password=password, )
        
        try:
    
            if user:
                customer=models.CustomerModel.objects.create(
                    user=user,
                    mobile=phone
                )
                msg={
                    'bool':True,
                    'user':user.id,
                    'customer':customer.id
                }
        except IntegrityError:
           
                msg={
                    'bool':False,
                    'user':"Mobile Already Exists"
                }
        
    except IntegrityError:
         msg={
                'bool':False,
                'user':"Username Already Exist"
            }


    return JsonResponse(msg)

@csrf_exempt
def addtocartfun(request):
    customer_id=request.POST.get('customer_id')
    product_id=request.POST.get('product_id')
    size_id=request.POST.get('size')
    customer=models.CustomerModel.objects.get(id=customer_id)
    product=models.Product.objects.get(id=product_id)
    size=models.Sizes.objects.get(id=size_id)
    addtocart=models.AddtoCarttt.objects.create(
        customer=customer,
        product=product,
        size=size,
        qty=1 

    )
    if addtocart:

      msg={
                    'bool':True,
                    'msg':"Added to cart"
                }
    else:
         msg={
                    'bool':False,
                    'msg':"Not added to carrt"
                }
    return JsonResponse(msg)

class OrderList(generics.ListCreateAPIView):#Responsible for listing and adding the data
    queryset = models.OrderModel.objects.all()
    serializer_class=serializers.Orderserializer


class OrderDetail(generics.ListAPIView):#responsible for fetching single data destroying the single data updating single data
    serializer_class=serializers.OrderItemserializer
    def get_queryset(self):
        order_id=self.kwargs['pk']
        order=models.OrderModel.objects.get(id=order_id)
        order_items=models.OrderItemsModel.objects.filter(order=order)
        return order_items
      
class CustomerAddress(viewsets.ModelViewSet):
    serializer_class=serializers.CustomerAdressSerializer
    queryset=models.CustomerAddress.objects.all()

class ProductRating(viewsets.ModelViewSet):
    serializer_class=serializers.ProductRatingSerializer
    queryset=models.ProductRating.objects.all()


class CategoryList(generics.ListCreateAPIView):#Responsible for listing and adding the data
    queryset = models.ProductCategory.objects.all()
    serializer_class=serializers.CategorySerializer
    


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):#responsible for fetching single data destroying the single data updating single data
    queryset = models.ProductCategory.objects.all()
    serializer_class=serializers.CategoryDetailSerializer

   