from django import forms
from .models import User
class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('phone_number', 'name', 'last_name', 'email',  'photo')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.is_admin = True  # Set is_admin to True by default
        if commit:
            user.save()
        return user





class UserChangeForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('phone_number', 'name', 'last_name', 'email', 'photo')

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
