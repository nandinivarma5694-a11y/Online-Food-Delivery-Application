from django.shortcuts import render,redirect
from .forms import SignupForm
from .models import Profile
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .forms import LoginForm
from .forms import CustomerForm

def home(request):
    context = {
        'name': 'home'
    }
    return render(request, 'core/home.html', context)
def food(request):
    return render(request, 'core/food.html')
def about(request):
    return render(request,'core/about.html')
def help(request):
    return render(request,'core/help.html')
def placeorder(request):
    return render(request,'core/placeorder.html')

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']

            # Check if email already exists
            if Profile.objects.filter(email=email).exists():
                messages.error(request, 'Email already registered. Please login or use another email.')
                form=signup_view(initial={'name':'Nandini','email':'nandiniverma@gmail.com','password':'12345678','city':'Mumbai'})
                return render(request, 'core/signup.html', {'form': form})

            # Create user with hashed password
            Profile.objects.create(
                name=form.cleaned_data['name'],
                email=email,
                password=make_password(form.cleaned_data['password']),
                city=form.cleaned_data['city']
            )

            messages.success(request, 'Account created successfully! Please login.')
            return redirect('login')  # Redirect to login page

    else:
        form = SignupForm(initial={'name':'Nandini','email':'nandiniverma@gmail.com','password':'12345678','city':'Mumbai'})

    return render(request, 'core/signup.html', {'form': form})





def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = Profile.objects.get(email=email)
                if check_password(password, user.password):
                    # Login successful, set session
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    messages.success(request, f'Welcome back, {user.name}!')
                    return redirect('home')  # Change 'home' to your homepage URL name
                else:
                    messages.error(request, 'Invalid password.')
            except Profile.DoesNotExist:
                messages.error(request, 'Email not registered.')
    else:
        form = LoginForm()

    return render(request, 'core/login.html', {'form': form})




def customer_details_view(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            # Save form data to session temporarily
            request.session['customer_data'] = form.cleaned_data
            return redirect('order_summary')
    else:
        form = CustomerForm()

    return render(request, 'core/customer_details.html', {'form': form})

def order_summary_view(request):
    customer_data = request.session.get('customer_data')
    if not customer_data:
        return redirect('customer_details')

    return render(request, 'core/order_summary.html', {'data': customer_data})
