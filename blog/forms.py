from django import forms
from .models import Post, Comment
from taggit.forms import TagWidget

class PostForm(forms.ModelForm):

    class Media:
        css = {
            'all': (
                'css/tag-it.min.css',
                'css/blog.css'
            )
        }
        js = (
            'https://code.jquery.com/ui/1.12.1/jquery-ui.min.js',
            'js/tag-it.min.js',
            'js/blog.js'
        )

    class Meta:
        model = Post
        fields = ('title', 'text', 'tags')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': TagWidget(attrs={'class': 'tagit-hidden-field', 'id': 'tag-it'}) 
        }

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)
        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
        }
