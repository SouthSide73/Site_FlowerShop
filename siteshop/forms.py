from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Имя'}
        )
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Email'}
        )
    )
    message = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Сообщение'}
        )
    )
    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': 'Номер телефона'}
        )
    )