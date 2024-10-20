from django import forms

class InputForm(forms.Form):
    json1= forms.CharField(widget=forms.Textarea(attrs={'name':'body', 'rows':10, 'cols':50}))
    json2 = forms.CharField(widget=forms.Textarea(attrs={'name':'body', 'rows':10, 'cols':50}))