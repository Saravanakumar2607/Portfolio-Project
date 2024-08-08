
from django import forms
from .models import  UserRegistration


class UserRegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="UserName")
    useremail = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), label="UserEmail")
    password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Password")
    confirm_password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Confirm Password")

    def _str_(self):
        return self.username
    

    class Meta:
        model = UserRegistration
        fields = '__all__'
        
        
# class UserLoginForm(forms.ModelForm):
#     username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="UserName")
#     password = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}), label="Password")


#     def _str_(self):
#         return self.username
    

#     class Meta:
#         model = UserLogin
#         fields = '__all__'
