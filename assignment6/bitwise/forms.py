from django import forms

class NumberInputForm(forms.Form):
    a = forms.FloatField(
        label='Number A',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number A'})
    )
    b = forms.FloatField(
        label='Number B',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number B'})
    )
    c = forms.FloatField(
        label='Number C',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number C'})
    )
    d = forms.FloatField(
        label='Number D',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number D'})
    )
    e = forms.FloatField(
        label='Number E',
        widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number E'})
    )

    def clean(self):
        cleaned_data = super().clean()
        
        # Verificar que todos los valores sean numéricos (Django ya lo hace)
        # Advertir si hay valores negativos
        for field_name in ['a', 'b', 'c', 'd', 'e']:
            value = cleaned_data.get(field_name)
            if value is not None and value < 0:
                self.add_error(field_name, f'Warning: {field_name} is negative')
        
        return cleaned_data