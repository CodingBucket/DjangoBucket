from django import forms
from blog.models import Post, Comments


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        widget = {
            'title': forms.Textarea
        }


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comments