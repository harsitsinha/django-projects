from django import forms

class CommentForm(forms.Form):
    username = forms.CharField()
    comment = forms.CharField(max_length=1000)
    