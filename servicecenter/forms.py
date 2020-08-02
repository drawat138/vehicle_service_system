from django import forms




from .models import CarServiceCenter, BikeServiceCenter, CarServiceRequest, BikeServiceRequest


class CarServiceRegistrationForm(forms.ModelForm):
    def clean_password(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return data
        else:
            raise forms.ValidationError("password and confirm password does not match")

    def clean_email(self):
        data = self.cleaned_data
        email = self.cleaned_data.get('email')
        qs = CarServiceCenter.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email already exists")
        else:
            return email

    def clean_phone(self):
        data = self.cleaned_data
        phone = self.cleaned_data.get('phone')
        qs = CarServiceCenter.objects.filter(phone=phone)
        if qs.exists():
            raise forms.ValidationError("Number already exists")
        else:
            return phone

    class Meta:
        model = CarServiceCenter
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter service-center name',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter moblie no',
            }),
            'alt_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter another no',
            }),

            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter password',
            }),
            'confirm_password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter confirm password',
            }),
            'gender': forms.Select(attrs={
                'class': 'form-control',

            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',

            }),
            'website': forms.TextInput(attrs={
                'class': 'form-control',

            }),
            'manufacturer': forms.Select(attrs={
                'class': 'form-control',

            }),
            'opening_time': forms.TextInput(attrs={
                'class': 'form-control',

            }),
            'closing_time': forms.TextInput(attrs={
                'class': 'form-control',

            }),
        }



class BikeServiceRegistrationForm(forms.ModelForm):
    def clean_password(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password == confirm_password:
            return data
        else:
            raise forms.ValidationError("password and confirm password does not match")

    def clean(self):
        data = self.cleaned_data
        email = self.cleaned_data.get('email')
        qs = BikeServiceCenter.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email already exists")
        else:
            return email

    class Meta:
        model = BikeServiceCenter
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter service-center name',
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter email'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter moblie no',
            }),
            'alt_phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter another no',
            }),

            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter password',
            }),
            'confirm_password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'placeholder': 'enter confirm password',
            }),
            'gender': forms.Select(attrs={
                'class': 'form-control',

            }),
            'address': forms.Textarea(attrs={
                'class': 'form-control',

            }),
            'website': forms.TextInput(attrs={
                'class': 'form-control',

            }),
            'manufacturer': forms.Select(attrs={
                'class': 'form-control',

            }),
            'opening_time': forms.TextInput(attrs={
                'class': 'form-control',

            }),
            'closing_time': forms.TextInput(attrs={
                'class': 'form-control',

            }),
        }
class CarLoginForm(forms.Form):
	username= forms.EmailField(widget=forms.TextInput(attrs={
		'class':'form-control',
		'placeholder':'enter email address',
		}))
	password= forms.CharField(widget=forms.PasswordInput(attrs={
		'class':'form-control',
		'placeholder':'enter password',
		}))

class BikeLoginForm(forms.Form):
	username= forms.EmailField(widget=forms.TextInput(attrs={
		'class':'form-control',
		'placeholder':'enter email address',
		}))
	password= forms.CharField(widget=forms.PasswordInput(attrs={
		'class':'form-control',
		'placeholder':'enter password',
		}))


class CarServiceForm(forms.ModelForm):
    class Meta:
        model = CarServiceRequest
        fields = ['vehicle_no','carservicecenter','bookedfor','bookdate','description','owned_by']

        widgets = {
            'vehicle_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '',
                'readonly':'readonly'
            }),
            'owned_by': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '',
                'readonly': 'readonly'
            }),
            'carservicecenter': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': ' ',
            }),
            'bookedfor': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': '',
            }),
            'bookdate': forms.TextInput(attrs={
                'class': 'form-control',


            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',


            }),



        }

class BikeServiceForm(forms.ModelForm):
    class Meta:
        model = BikeServiceRequest
        fields = ['vehicle_no','bikeservicecenter','bookedfor','bookdate','description','owned_by']

        widgets = {
            'vehicle_no': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '',
                'readonly':'readonly'
            }),
            'owned_by': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '',
                'readonly': 'readonly'
            }),
            'carservicecenter': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': ' ',
            }),
            'bookedfor': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': '',
            }),
            'bookdate': forms.TextInput(attrs={
                'class': 'form-control',


            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',


            }),



        }