from django import forms

from .models import Comment

class SnippetForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = "__all__"
    