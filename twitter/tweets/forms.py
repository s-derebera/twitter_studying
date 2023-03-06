from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    tweet_text = forms.CharField(required=True, widget=forms.widgets.Textarea(
        attrs={
        "placeholder": "Create your new Tweet", "class": "form-control",
        }
    ),
    label='',)

    class Meta:
        model = Tweet
        exclude = ("pub_date",)