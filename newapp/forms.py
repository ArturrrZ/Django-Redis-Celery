from django import forms

class EmailForm(forms.Form):
    subject = forms.CharField(max_length=50, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Subject'
    }))
    body = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Your message',
        'rows':'5',
        'cols':'10',
        'class': 'form-control'
    }))
    recipient = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Recipient email: example@gmail.com',
        'class': 'form-control'
    }))