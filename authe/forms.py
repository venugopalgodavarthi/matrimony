from django import forms
from authe.models import registermodel
from django.contrib.auth.hashers import make_password
class registerform(forms.ModelForm):
    class Meta:
        model=registermodel
        fields=['username','first_name','last_name','email','phone','age','gender','dob','password']
        widgets={'password':forms.PasswordInput}
    repassword=forms.CharField(widget=forms.PasswordInput)
    def save(self,commit=True):
        user=super().save(commit=False)
        user.password=make_password(self.cleaned_data['password'])
        if commit==True:
            user.save()
        return user
    def clean(self):
        pas=self.cleaned_data['password']
        rpas=self.cleaned_data['repassword']
        if not(pas == rpas):
            raise forms.ValidationError('password and repassword should be same')

        age=self.cleaned_data['age']
        if not(16<=age<=65):
            raise forms.ValidationError('age should be min 16 years max 65 years')
        
        if not(3<=len(pas)<=10):
            raise forms.ValidationError('password should be min 3 characters max 10 characters')
        


class loginform(forms.Form):
    username=forms.CharField()
    password=forms.CharField()