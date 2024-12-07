from django import forms

from django.contrib.auth.forms import UserCreationForm

from store.models import User,Order

class SignUpForm(UserCreationForm):

    class Meta:

        model=User

        fields=["username","email","phone","password1","password2"]

        widgets={
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "password1":forms.TextInput(attrs={"class":"form-control"}),
            "password2":forms.TextInput(attrs={"class":"form-control"}),
            "phone":forms.NumberInput(attrs={"class":"form-control"}),
            
                 }      


class SignInForm(forms.Form):

    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))

    password=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))


    
class OrderForm(forms.ModelForm):

    class Meta:

        model=Order

        fields=["address","phone","payment_method"]