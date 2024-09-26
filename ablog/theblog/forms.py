from django import forms
from .models import Post


# this is done to modify form style

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_page','author','body')
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_page':forms.TextInput(attrs={'class':'form-control'}),
            'author':forms.Select(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),

        }

class EditForms(forms.ModelForm):
    class Meta:
        model=Post
        fields=('title','title_page','body')
        widgets= {
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'title_tag':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'})
        }