from this import d
from django import forms
from prodetail.models import details,education,profilelink,family,address, siblings,occupation

class detailsform(forms.ModelForm):
    class Meta:
        model=details
        fields='__all__'
    def clean(self):
        name=self.cleaned_data['surname']
        if not(3<=len(name)<=15):
            raise forms.ValidationError('surname should be min 3 characters and max 15 characters')
        

class educationform(forms.ModelForm):
    class Meta:
        model=education
        fields='__all__'

class occupationform(forms.ModelForm):
    class Meta:
        model=occupation
        fields='__all__'

class profilelinkform(forms.ModelForm):
    class Meta:
        model=profilelink
        fields='__all__'


class familyform(forms.ModelForm):
    class Meta:
        model=family
        fields='__all__'

class sibilingsform(forms.ModelForm):
    class Meta:
        model=siblings
        fields='__all__'

class addressform(forms.ModelForm):
    class Meta:
        model=address
        fields='__all__'