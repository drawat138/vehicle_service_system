from django import forms
from .models import CarManufacturer,BikeManufacturer

class CarManufacturerForm(forms.ModelForm):
	class Meta:
		model=CarManufacturer
		fields=['manufacturer_name']
		widgets={
		'manufacturer_name':forms.TextInput(attrs={
			'class':'form-control',
			'placeholder':'enter manufacturer_name',
			'readonly':'readonly'
			})
		}
class BikeManufacturerForm(forms.ModelForm):
	class Meta:
		model=BikeManufacturer
		fields=['manufacturer_name']
		widgets={
		'manufacturer_name':forms.TextInput(attrs={
			'class':'form-control',
			'placeholder':'enter manufacturer_name',
			'readonly':'readonly'
			})
		}


		