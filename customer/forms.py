from django import forms
from .models import Register,CarVehicle,BikeVehicle
class RegistrationForm(forms.ModelForm): 
	# def clean_password(self):
	# 	data=self.cleaned_data
	# 	password=self.cleaned_data.get('password')
	# 	confirm_password=self.cleaned_data.get('confirm_password')
	# 	if password==confirm_password:
	# 		return data
	# 	else:
	# 		raise forms.ValidationError("password not matched")



	def clean_email(self):
		data=self.cleaned_data
		email=self.cleaned_data.get('email')
		qs=Register.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError("Email already exists")
		else:
			return email
	def clean_phone(self):
		data=self.cleaned_data
		phone=self.cleaned_data.get('phone')
		qs=Register.objects.filter(phone=phone)
		if qs.exists():
			raise forms.ValidationError("Number already exists")
		else:
			return phone


	class Meta:
		model=Register
		fields='__all__'
		widgets={
			'city':forms.Select(attrs={'class':'form-control'}),
			'name':forms.TextInput(attrs={
		           'class':'form-control',
		           'placeholder':'enter name',
		           }),
			'email':forms.TextInput(attrs={
				'class':'form-control',
				'placeholder':'enter email'
				}),
			'phone':forms.TextInput(attrs={
		        'class':'form-control',
		        'placeholder':'enter moblie no',
		        }),
			'alt_phone':forms.TextInput(attrs={
		        'class':'form-control',
		        'placeholder':'enter moblie no',
		        }),
			'password':forms.PasswordInput(attrs={
		        'class':'form-control',
		        'placeholder':'enter password',
		        }),
			'confirm_password':forms.PasswordInput(attrs={
		        'class':'form-control',
		        'placeholder':'enter confirm password',
		        }),
			'gender':forms.Select(attrs={
		        'class':'form-control',
		 
		        }),
            'home_address':forms.Textarea(attrs={
		        'class':'form-control',
		        'placeholder':'enter address',
		        }),
			'vehicle_delivery_address': forms.Textarea(attrs={
				'class': 'form-control',
				'placeholder': 'enter address',
			}),

		}
class LoginForm(forms.Form):
	username= forms.EmailField(widget=forms.TextInput(attrs={
		'class':'form-control',
		'placeholder':'enter email address',
		}))
	password= forms.CharField(widget=forms.PasswordInput(attrs={
		'class':'form-control',
		'placeholder':'enter password',
		}))


class CarRegistration(forms.ModelForm):
	class Meta:
		model=CarVehicle
		fields='__all__'
		widgets={
			'vehicle_no':forms.TextInput(attrs={
		           'class':'form-control',
		           'placeholder':' ',
		           }),
			'manufacturer_name':forms.Select(attrs={
		           'class':'form-control',
		           'placeholder':' ',
		           }),
			'vehicle_type':forms.TextInput(attrs={
		           'class':'form-control',
				   'readonly':'readonly'
		           
		           }),
			'model_name':forms.TextInput(attrs={
		           'class':'form-control',
		           'placeholder':' ',
		           }),
			'owned_by':forms.TextInput(attrs={
		           'class':'form-control',
		           'placeholder':' ',
				  'readonly':'readonly'
		           }),
			
            }
class BikeRegistration(forms.ModelForm):
	class Meta:
		model=BikeVehicle
		fields='__all__'
		widgets={
			'vehicle_no':forms.TextInput(attrs={
		           'class':'form-control',
		           'placeholder':' ',
		           }),
			'manufacturer_name':forms.Select(attrs={
		           'class':'form-control',
		           'placeholder':' ',
		           }),
			'vehicle_type':forms.TextInput(attrs={
		           'class':'form-control',
				'readonly': 'readonly'
		           
		           }),
			'model_name':forms.TextInput(attrs={
		           'class':'form-control',
		           'placeholder':' ',
		           }),
			'owned_by':forms.TextInput(attrs={
		           'class':'form-control',
		           'placeholder':' ',
				  'readonly':'readonly'
		           }),
			
         }
 


