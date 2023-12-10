from django import forms
from .models import Comment
from django.contrib.auth.models import User
from .models import Post,UserProfile

# Add your form here


class AddComment(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

        widgets = {
            'post': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'}),
            'comment_text': forms.Textarea(attrs={'class': 'form-control'})
        }
        labels = {
            'comment_text': ''
        }


class AddUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'})

        }
        labels = {
            'username': 'Enter Your User Name',
            'first_name': 'Enter Your First Name',
            'last_name': 'Enter Your Last Name',
            'email': 'Enter Your Email',
            'password': 'Enter Your Password',
        }


class EditProfile(AddUser):
    class Meta:
        model=UserProfile
        fields='__all__'

        widgets = {
            'user': forms.TextInput(attrs={'class': 'form-control','type':'hidden'}),
            'bio': forms.TextInput(attrs={'class': 'form-control'}),
            'fb_url': forms.TextInput(attrs={'class': 'form-control'}),
            'insta_url': forms.TextInput(attrs={'class': 'form-control'}),

        }
        labels = {
            'bio': 'Enter Your Bio',
            'fb_url': 'Facebook url',
            'insta_url': 'Instagram url',

        }
class EditUserProfile(AddUser):pass
    

class AddPost(forms.ModelForm):
    class Meta:
        model = Post

        fields = ['title', 'body', 'author']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'type': 'hidden'})

        }


class EditPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', }),

        }
