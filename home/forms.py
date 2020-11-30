from django import forms
from . models import Test


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = (
            'title',
            'subtitle',
            'quantity',
        )
        widgets = {
            'title':forms.TextInput(
                attrs={
                    'placeholder':'Type title...',
                    'class':'form-control'
                }
            ),
            'subtitle':forms.TextInput(
                attrs={
                    'placeholder':'Type subtitle...',
                    'class':'form-control'
                }
            ),
            'quantity':forms.TextInput(
                attrs={
                    'placeholder':'Type quantity...',
                    'class':'form-control'
                }
            )
        }

    #Validad el numero que se digite en quantity
    def clean_quantity(self):
        quant = self.cleaned_data['quantity']
        
        if quant < 10:
            raise forms.ValidationError('Ingrese un numero mayor que 10')
        return quant
