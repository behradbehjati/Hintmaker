from .models import User
from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import  ReadOnlyPasswordHashField
import django.contrib.auth.password_validation as validators

class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confiirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = '__all__'

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = '__all__'
class RegisterForm(forms.Form):
    name=forms.CharField(max_length=200,label='Name')
    email=forms.EmailField()
    phone_number = forms.CharField(max_length=11, label='Phone number')
    password=forms.CharField(widget=forms.PasswordInput)
    def clean_email(self):
        email=self.cleaned_data['email']
        user=User.objects.filter(email=email).exists()
        if user:
            raise ValidationError('This email already exists')
        return email
    def clean_phone_number(self):
        phone_number=self.cleaned_data['phone_number']
        user=User.objects.filter(phone_number=phone_number).exists()
        if user:
            raise ValidationError('This phone number already exists')
        return phone_number
    def clean_password(self):
        password=self.cleaned_data['password']
        validators.validate_password(password=password)
        return password
class LoginForm(forms.Form):
    email=forms.EmailField()
    password=forms.CharField(max_length=100)
    remember_me=forms.BooleanField()
class ProfileEditForm(forms.ModelForm):
    email=forms.EmailField(disabled = True)
    password=forms.CharField(disabled = True,widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['email','name','phone_number','password']




