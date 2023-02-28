from django import forms
from django.forms import ModelForm,Textarea
from .models import MakeHint
from emoji_picker.widgets import EmojiPickerTextInputAdmin, EmojiPickerTextareaAdmin
class MakeHintForm(ModelForm):
    class Meta:
        model=MakeHint
        fields=['site_name','password_type','hint']
        widgets = {
            'hint': Textarea(attrs={'id': 'hintmaker'})
        }


class EditForm(ModelForm):
    class Meta:
        model=MakeHint
        fields=['site_name','password_type','hint']
        widgets = {
            'hint': Textarea(attrs={'id': 'hintmaker'})
        }





