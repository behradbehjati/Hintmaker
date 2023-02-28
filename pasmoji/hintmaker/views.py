from django.shortcuts import render,redirect,get_object_or_404
from django.views import View
from .forms import MakeHintForm,EditForm
from  accounts.forms import RegisterForm
from .models import MakeHint
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.decorators import login_required



class HintMakerView(View):
    form_class=MakeHintForm
    def get(self,request):
        form=self.form_class()
        return render(request,'hintmaker/hint-maker.html',{'form':form})
    def post(self,request):
        form=self.form_class(request.POST)

        if ( not request.user.is_authenticated) and form.is_valid():
                cd = form.cleaned_data
                request.session['hint']={
                    'site_name':cd['site_name'],
                    'password_type':cd['password_type'],
                    'hint':cd['hint']
                }



                return redirect('accounts:register')
        else:
                if form.is_valid():
                    new_hint = form.save(commit=False)
                    new_hint.slug='svfvf'
                    new_hint.user=request.user
                    new_hint.save()
                    messages.add_message(request, messages.INFO, 'Hello world.')
                    return redirect('hintmaker:hintmaker')

        return redirect('hintmaker:home')




class HomeView(View):
    def get(self,request):
        return render(request,'home/home.html')
class EditView(View):
    def dispatch(self,request,*args,**kwargs):
        if request.user != get_object_or_404(MakeHint,id=kwargs['id']).user:
            messages.error(request, 'not allowed')
            return redirect('hintmaker:hintmaker')
        return super().dispatch(request, *args, **kwargs)
    form_class=EditForm
    def get(self,request ,id):
        hint=get_object_or_404(MakeHint,id=id)
        form = self.form_class(instance=hint)
        return render(request, 'hintmaker/edit.html', {'form': form})

    def post(self, request,id):
        hint = get_object_or_404(MakeHint, id=id)
        form = self.form_class(request.POST, instance=hint)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your hint has been updated')
            return redirect('accounts:profile')
        return redirect('hintmaker:edit', hint.id)





