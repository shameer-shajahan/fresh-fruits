from django.shortcuts import render,redirect,get_object_or_404

from django.views import View

from store.forms import SignUpForm,SignInForm,OrderForm

from django.contrib.auth import authenticate,login,logout

from store.models import Product,BasketItem,OrderItem

class SignUpView(View):

    template_name="signup.html"

    form_class=SignUpForm

    def get(self,request,*arg,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})

    def post(self,request,*args,**kwargs):

        form_data=request.POST 

        form_instance=self.form_class(form_data)

        if form_instance.is_valid():

            form_instance.save()

            return redirect("signin")

        print("account creation failed")

        return render(request,self.template_name,{"form":form_instance})

class SignInView(View):

    template_name="signin.html"

    form_class=SignInForm


    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        return render(request,self.template_name,{"form":form_instance})

    def post(self,request,*args,**kwargs):

        form_data=request.POST 

        form_instance=self.form_class(form_data)

        if form_instance.is_valid():

            data=form_instance.cleaned_data

            uname=data.get("username")

            pwd=data.get("password")

            user_obj=authenticate(request,username=uname,password=pwd)

            if user_obj:

                login(request,user_obj)


                return redirect("products-list")


        return render(request,self.template_name,{"form":form_instance})

class SignOutView(View):

    def get(self,request,*args,**kwargs):

        logout(request)

        return redirect("signin")
    
class ProductListView(View):

    template_name="index.html"

    def get(self,request,*args,**kwargs):

        qs=Product.objects.all()

        return render(request,self.template_name,{"data":qs})
    
class ProductDetailView(View):

    template_name="product_detail.html"

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        qs=Product.objects.get(id=id)

        return render(request,self.template_name,{"product":qs})

class AddToCartView(View):

    def post(self,request,*args,**kwargs):

        id=kwargs.get('pk')

        size=request.POST.get("size") 

        quantity=request.POST.get("quantity")

        product_object=Product.objects.get(id=id)

        basket_object=request.user.cart

        BasketItem.objects.create(
            
            product_object=product_object,
            
            quantity=quantity,
            
            basket_object=basket_object
        )

        print("item has been added to cart")

        return redirect("cart-summary")   

class CartSummaryView(View):

    template_name="cart_summary.html"

    def get(self,request,*args,**kwargs):

        qs=BasketItem.objects.filter(basket_object=request.user.cart,is_order_placed=False)
    
        Basket_total=sum([bi.item_total for bi in qs])

        return render(request,self.template_name,{"basket_items":qs,"basket_total":Basket_total})          

class ItemDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        BasketItem.objects.get(id=id).delete()

        return redirect("cart-summary")

class PlaceOrderView(View):

    form_class=OrderForm

    template_name="place_order.html"

    def get(self,request,*args,**kwargs):

        form_instance=self.form_class()

        qs=request.user.cart.cart_item.filter(is_order_placed=False)

        basket_item=BasketItem.objects.filter(basket_object=request.user.cart,is_order_placed=False)

        Basket_total=sum([bi.item_total for bi in qs])

        return render(request,self.template_name,{"form":form_instance, "items":qs , "basket_total":Basket_total})

    def post(self,request,*args,**kwargs):

        form_data=request.POST 

        form_instance=self.form_class(form_data)

        if form_instance.is_valid():

            form_instance.instance.customer=request.user

            order_instance=form_instance.save()

            basket_item=request.user.cart.cart_item.filter(is_order_placed=False)

            payment_method=form_instance.cleaned_data.get("payment_method")

            for bi in basket_item:

                OrderItem.objects.create(
                    order_object=order_instance,
                    product_object=bi.product_object,
                    quantity=bi.quantity,
                    price=bi.product_object.price
                )

                bi.is_order_placed=True

                bi.save()

        
        return redirect("order-summary")

class OrderSummeryView(View):

    template_name="order_summery.html"

    def get(self,request,*args,**kwargs):

        qs=request.user.orders.all().order_by("-created_date")

        return render (request,self.template_name,{"orders":qs})
    
