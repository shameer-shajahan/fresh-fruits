from django.db import models

from django.contrib.auth.models import AbstractUser 

from django.db.models.signals import post_save

# from random import randint

class User(AbstractUser):

    phone=models.CharField(max_length=15,unique=True)

class BaseModel(models.Model):

    created_date=models.DateTimeField(auto_now_add=True)

    updated_date=models.DateTimeField(auto_now=True)

    is_active=models.BooleanField(default=True)

class Varieties(BaseModel):

    name=models.CharField(max_length=200)

    def __str__(self):

        return self.name
  
class Product(BaseModel):

    title=models.CharField(max_length=200)

    description=models.TextField()

    price=models.PositiveIntegerField()

    picture=models.ImageField(upload_to="product_images",null=True,blank=True)



    Varieties_object=models.ForeignKey(Varieties,on_delete=models.CASCADE,default=None)

    # category_object=models.ForeignKey(Category,on_delete=models.CASCADE)

    # size_objects=models.ManyToManyField(Size)

    # tag_objects=models.ManyToManyField(Tag)

    # color=models.CharField(max_length=200)


    def __str__(self):
        
        return self.title
    
class Basket(BaseModel):

    owner=models.OneToOneField(User,on_delete=models.CASCADE,related_name="cart")
    
class BasketItem(BaseModel):

    product_object=models.ForeignKey(Product,on_delete=models.CASCADE)

    quantity=models.PositiveIntegerField(default=1)

    # size_object=models.ForeignKey(Size,on_delete=models.CASCADE)

    is_order_placed=models.BooleanField(default=False)

    basket_object=models.ForeignKey(Basket,on_delete=models.CASCADE,related_name="cart_item")

    @property
    def item_total(self):

        return self.product_object.price*self.quantity


def create_basket(sender,instance,created,**kwargs):

    if created:

        Basket.objects.create(owner=instance)

post_save.connect(create_basket,User)



class Order(BaseModel):

    customer=models.ForeignKey(User,on_delete=models.CASCADE,related_name="orders")

    address=models.TextField()

    phone=models.CharField(max_length=20)

    PAYMENT_OPTIONS=(
        ("COD","COD"),
        ("ONLINE","ONLINE")
    )

    payment_method=models.CharField(max_length=15,choices=PAYMENT_OPTIONS,default="COD")

    is_paid=models.BooleanField(default=False)

    def order_total(self):
        
        total=sum([oi.item_total for oi in self.orderitems.all()])

        return total
    
    @property
    def item_total(self):

        return self.price*self.quantity


class OrderItem(BaseModel):

    order_object=models.ForeignKey(
                                   Order,on_delete=models.CASCADE,
                                   related_name="orderitems"
                                   )
    
    product_object=models.ForeignKey(Product,on_delete=models.CASCADE)

    quantity=models.PositiveIntegerField(default=1)

    price=models.FloatField()

    @property
    def item_total(self):

        return self.price*self.quantity
    