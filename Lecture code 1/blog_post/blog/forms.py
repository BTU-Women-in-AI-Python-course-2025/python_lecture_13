from django import forms


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
