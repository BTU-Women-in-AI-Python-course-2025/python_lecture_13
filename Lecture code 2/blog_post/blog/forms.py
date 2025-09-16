from django import forms


class BlogPostForm(forms.Form):
    title = forms.CharField(
        label="Title",
        max_length=100,
    )
    text = forms.CharField(
        label="Text",
        help_text="Enter a valid email address.",
        widget = forms.TextInput(attrs={'class': 'form-control'})
    )
    created_at = forms.DateTimeField(
        label='Created at',
        widget=forms.DateTimeInput(
            attrs={
                'type': 'datetime-local',
                'class': 'form-control'
            }
        )
    )
    is_active = forms.BooleanField(label="Is active")
