from django import forms
from blog.models import BlogPost


class BlogPostForm(forms.Form):
    title = forms.CharField(label="Title", max_length=255)
    text = forms.CharField(label="Text")
    active = forms.BooleanField(label="Active")
    create_date = forms.DateTimeField(
        label="Create date",
        widget=forms.DateTimeInput(
            attrs={
                "type": "datetime-local",
                "class": "form-control"
            }
        ),
    )


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'text', 'active', 'document']
