from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,logout,login
from django.views import View
from .forms import RegisterForm,LoginForm,ProfileEditForm
from .models import User
from hintmaker.models import MakeHint
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from .utils import get_url_image
from django.contrib.auth import views

class RegisterView(View):
    form_class = RegisterForm
    def dispatch(self,request,*args,**kwargs):
        if request.user.is_authenticated:
            messages.error(request, 'dispatch error')
            return redirect('hintmaker:hintmaker')
        return super().dispatch(request, *args, **kwargs)


    def get(self,request):

        form=self.form_class()
        return render(request,'accounts/register.html',{'form':form})
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            User.objects.create_user(email=cd['email'],phone_number=cd['phone_number'],password=cd['password'],name=cd['name'])


            user = authenticate(email=form.cleaned_data['email'], password=form.cleaned_data['password'])
            login(request,user)
            session=request.session.get('hint')
            print(session)
            if session:

                MakeHint.objects.create(site_name=session['site_name'],password_type=session['password_type'],hint=session['hint'],slug='fvfv',user=user)
                return redirect('accounts:profile')

            else:

             return redirect('hintmaker:hintmaker')
        return render(request,'accounts/register.html',{'form':form})
class LoginView(View):
    form_class=LoginForm
    def get(self,request):
        form=self.form_class()
        return render(request,'accounts/login.html',{'form':form})
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            user = authenticate(email=cd['email'], password=cd['password'])
            if user:
                if cd['remember_me']:
                  request.session.set_expiry(1209600)
                else:
                  request.session.set_expiry(0)
                login(request,user)
                session=request.session.get('hint')
                if session:

                    MakeHint.objects.create(site_name=session['site_name'], password_type=session['password_type'],
                                     hint=session['hint'])
                    return redirect('hintmaker:home')
                elif  'next' in request.GET:
                   return redirect(request.GET.get('next'))

                else:

                    return redirect('accounts:profile')
            else:
                messages.error(request, 'Email or Password is incorrect')
                return redirect('accounts:login')
        return redirect('hintmaker:hintmaker')
class LogoutView(views.LogoutView):
    def __init__(self):
        self.next_page='accounts:login'



class ProfileView(LoginRequiredMixin,View):
    def get(self,request):
        hints=MakeHint.objects.filter(user=request.user)

        return render(request,'accounts/profile.html',{'hints':hints,})
# class N_LoginView(views.LoginView):
#     def __init__(self):
#         self.template_name='accounts/login.html'
#         self.next_page='accounts:profile'
class PasswordResetView(views.PasswordResetView):
    def __init__(self):
        self.template_name='accounts/email/password_reset_view.html'
        self.email_template_name='accounts/email/password_reset_email.html'
        self.subject_template_name='accounts/email/password_reset_subject.txt'
        self.success_url='done/'
class PasswordResetConfirmView(views.PasswordResetConfirmView):
    def __init__(self):
        self.template_name='accounts/email/password_reset_confirm.html'
        self.success_url='password_reset_complete/'
class ProfileEditView(LoginRequiredMixin,View):
    form_class=ProfileEditForm
    def get(self,request):
        user=request.user
        form=self.form_class(instance=user)
        return render(request,'accounts/profile_edit.html',{'form':form})
    def post(self,request):
        user = request.user
        form=self.form_class(request.POST,instance=user)
        if form.is_valid():
            form.save()
            messages.success(request,'You change your profile')
            return redirect('accounts:profile')
        return redirect('accounts:profile_edit')

















