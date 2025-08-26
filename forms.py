from django import forms

class SignupForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    city = forms.CharField(max_length=70)


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

# forms.py

from django import forms

class CustomerForm(forms.Form):
    name = forms.CharField(max_length=100)
    phone = forms.CharField(max_length=10)
    email = forms.EmailField(required=False)
    address = forms.CharField(widget=forms.Textarea)
    city = forms.CharField(max_length=50)
    pincode = forms.CharField(max_length=6)
    payment = forms.ChoiceField(choices=[
        ('cod', 'Cash on Delivery'),
        ('upi', 'UPI'),
        ('card', 'Credit/Debit Card'),
    ])

'''
class Registration(form.ModelForm):
    class Meta:
        model=Profile
        fields=['name','email','password' ]
        #labels={'name':'name','email':'Enter Email'}
        error_message={
            'email':{'required':'Email is required'}
        }
        widgets={
            'password':forms.PasswordInput(attrs={'class':'pwdclass'}),
            'name':forms.TextInput(attrs={'class':'mtclass','placeholder':'Enter your name'})
            'email':forms.EmailField(attrs={'placeholder':'Enter your email'})
        }
'''