from django import forms
from . import models
class EmailMaterialForm(forms.Form):
    name = forms.CharField(max_length=20)
    my_email = forms.EmailField()
    to_email = forms.EmailField()
    comment = forms.CharField(required=False,
                              widget=forms.Textarea)


class MaterialForm(forms.ModelForm):
    class Meta:
        model = models.Material
        fields = ('title', 'body', 'material_type')