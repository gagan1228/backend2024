from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Vendor(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    address=models.TextField(null=True)
    phone=models.TextField(null=True)
    isverified=models.BooleanField(default=False)
    def __str__(self) :
        return self.user.username
    

class ProductCategory(models.Model):
    title=models.CharField(max_length=200)
    detail=models.TextField(null=True)
    def __str__(self) :
        return self.title

class Product(models.Model):
    category=models.ForeignKey(ProductCategory,on_delete=models.SET_NULL,null=True,related_name='category_product')
    vendor=models.ForeignKey(Vendor,on_delete=models.SET_NULL,null=True)
    title=models.CharField(max_length=200)
    detail=models.TextField(null=True)
    price=models.FloatField()

    def __str__(self) :
        return self.title
    

class CustomerModel(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile=models.PositiveBigIntegerField(unique=True)

    def __str__(self):
        return self.user.username
    
class OrderModel(models.Model):
    customer=models.ForeignKey(CustomerModel,on_delete=models.CASCADE)
    order_time=models.DateTimeField(auto_now_add=True)



class OrderItemsModel(models.Model):
    order=models.ForeignKey(OrderModel,on_delete=models.CASCADE,related_name='order_items')
    product=models.ForeignKey(Product,on_delete=models.CASCADE)

    def __str__(self) :
        return self.order.customer.user.username 


class CustomerAddress(models.Model):
    customer=models.ForeignKey(CustomerModel,on_delete=models.CASCADE,related_name='Customer_addresses')
    address=models.TextField()
    default_address=models.BooleanField(default=False)
    def __str__(self) :
        return self.address
    

class Sizes(models.Model):
    size=models.CharField(max_length=20)
    def __str__(self) :
        return self.size
    
class AddtoCarttt(models.Model):
    customer=models.ForeignKey(CustomerModel,on_delete=models.CASCADE)
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    size=models.ForeignKey(Sizes,on_delete=models.CASCADE)
    qty=models.IntegerField()

    def __str__(self):
        return self.customer.user.username

    


class ProductRating(models.Model):
    customer=models.ForeignKey(CustomerModel,on_delete=models.CASCADE,related_name='rating_customers')
    product=models.ForeignKey(Product,on_delete=models.CASCADE,related_name='product_ratings')
    ratings=models.IntegerField()
    reviews=models.TextField()
    add_time=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.ratings} - {self.reviews}'