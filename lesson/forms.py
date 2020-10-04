from django import forms

class EmailMaterialForm(forms.Form):
    name = forms.CharField(max_length=20)
    my_email = forms.EmailField()
    to_email = forms.EmailField()
    comment = forms.CharField(required=False,
                              widget=forms.Textarea)
