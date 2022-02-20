from django import forms

class AddPostForm(forms.Form):
    post_title = forms.CharField(max_length=200)
    post_description = forms.CharField(max_length=300, widget=forms.Textarea)
    post_message = forms.CharField(max_length=5000,  widget=forms.Textarea)