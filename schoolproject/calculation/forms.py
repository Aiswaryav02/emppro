from django import forms

class Subform(forms.Form):
    fnum=forms.IntegerField(label="Enter First Number")
    snum=forms.IntegerField(label="Enter First Number")
    def clean(self):
        cleaned_data=super().clean()
        n1=cleaned_data.get('fnum')
        n2=cleaned_data.get('snum')
        if n1<0:
            msg="Invalid value"
            self.add_error("fnum",msg)
        if n2<0:
            msg="Invalid"
            self.add_error("snum",msg)
        
class Strcnts(forms.Form):
    sen=forms.CharField(label="Enter First sentence")
    