from logging import PlaceHolder
from django import forms
from .models import Article, JobApplication
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 #  --------------------------------- DONE -----------------------------
class ArticleForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={
        'class':'post-title', 'placeholder':'title'
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class':'post-details','placeholder':'description'
    }))
    photo_article = forms.ImageField(widget=forms.FileInput(attrs={'class': 'post-thumb'}))

    class Meta:
        fields=['title','description','photo_article']
        model = Article


class RegisterForm(UserCreationForm):

    email = forms.EmailField(max_length=254)
    class Meta:
        model = User
        fields=('username','email','password1','password2')




class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['name', 'email', 'portfolio_link', 'github_link', 'about']
        widgets = {
            'about': forms.Textarea(attrs={'rows': 10, 'placeholder': 'Write Something About You'}),
        }
