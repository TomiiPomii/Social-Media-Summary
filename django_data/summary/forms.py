from django import forms


class UrlForm(forms.Form):
    twitter_url = forms.URLField(label='Twitter profil URL', max_length=1000)