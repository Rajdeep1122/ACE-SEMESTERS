from django import forms
from .models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    """
    Form for creating and updating blog posts.
    """
    class Meta:
        model = Post
        fields = ('title', 'category', 'content')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'category': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500'}),
            'content': forms.Textarea(attrs={'class': 'w-full h-40 px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500', 'rows': 10}),
        }

class SignUpForm(UserCreationForm):
    """
    Form for user registration.
    """
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
