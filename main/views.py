# from django.shortcuts import render, redirect
# import time

# def splash(request):
#     time.sleep(2)  # Optional delay for splash screen effect
#     return render(request, 'main/splash.html')
# main/views.py
# from django.shortcuts import render, redirect
# import time

# def splash(request):
#     time.sleep(2)  # Optional delay for splash screen effect
#     return render(request, 'main/splash.html')

# def home(request):
#     return render(request, 'main/home.html')

# def signup(request):
#     return render(request, 'main/signup.html')

# def forgot_password(request):
#     return render(request, 'main/forgot_password.html')

# def select_role(request):
#     return render(request, 'main/select_role.html')
# from django.shortcuts import render, redirect
# import time

# def splash(request):
#     time.sleep(2)  # Optional delay for splash screen effect
#     return render(request, 'main/splash.html')

# def home(request):
#     return render(request, 'main/home.html')

# def signup(request):
#     if request.method == 'POST':
#         # Handle signup logic here (e.g., saving user data)
#         pass
#     return render(request, 'main/signup.html')

# def forgot_password(request):
#     if request.method == 'POST':
#         # Handle forgot password logic here (e.g., sending reset email)
#         pass
#     return render(request, 'main/forgot_password.html')

# def role_selection(request):
#     return render(request, 'main/role_selection.html')

# def patient(request):
#     return render(request, 'main/patient.html')

# def doctor(request):
#     return render(request, 'main/doctor.html')

# def pharmacy(request):
#     return render(request, 'main/pharmacy.html')
# main/views.py

# from django.template.loader import get_template
# from django.shortcuts import render, redirect
# from django.contrib.auth import login, authenticate
# from django.contrib.auth import logout
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib import messages
# from django.utils.decorators import method_decorator
# from django.shortcuts import render, get_object_or_404
# from .models import UserProfile
# import time

# get_template('main/base.html')  # This should not raise an error

# def splash(request):
#     time.sleep(2)  # Optional delay for splash screen effect
#     return render(request, 'main/splash.html')

# def home(request):
#     return render(request, 'main/home.html')

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 messages.success(request, 'Registration successful. Welcome!')
#                 return redirect('home')
#             else:
#                 messages.error(request, 'Registration error. Please try again.')
#     else:
#         form = UserCreationForm()
    
#     return render(request, 'main/signup.html', {'form': form})

# def forgot_password(request):
#     if request.method == 'POST':
#         # Handle password reset logic here (e.g., sending reset email)
#         messages.success(request, 'Password reset email sent! Please check your inbox.')
#         return redirect('home')
#     return render(request, 'main/forgot_password.html')

# def role_selection(request):
#     return render(request, 'main/role_selection.html')

# def patient(request):
#     return render(request, 'main/patient.html')

# def doctor(request):
#     return render(request, 'main/doctor.html')

# def pharmacy(request):
#     return render(request, 'main/pharmacy.html')

# def login_view(request):
#     # Your login logic here
#     return render(request, 'login.html')

# def logout_view(request):
#     logout(request)
#     return redirect('home')  # Redirect to a desired page after logout

# def user_details(request):
#     user_profile = get_object_or_404(UserProfile, user=request.user)
#     context = {
#         'user_profile': user_profile,
#         'medicines': user_profile.medicines.all(),
#     }
#     return render(request, 'main/user_details.html', context)
from django.template.loader import get_template
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import UserProfile, Role  # Ensure Role is imported
import time

get_template('main/base.html')  # This should not raise an error

def splash(request):
    time.sleep(2)  # Optional delay for splash screen effect
    return render(request, 'main/splash.html')

def home(request):
    return render(request, 'main/home.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                # Assuming role_id is being passed from the signup form
                role_id = request.POST.get('role')  
                role = Role.objects.get(id=role_id)  # Fetch the role object
                user_profile = UserProfile(user=user, role=role)
                user_profile.save()
                login(request, user)
                messages.success(request, 'Registration successful. Welcome!')
                return redirect('home')
            else:
                messages.error(request, 'Registration error. Please try again.')
    else:
        form = UserCreationForm()
    
    roles = Role.objects.all()  # Get all roles to display in the form
    return render(request, 'main/signup.html', {'form': form, 'roles': roles})

def forgot_password(request):
    if request.method == 'POST':
        # Handle password reset logic here (e.g., sending reset email)
        messages.success(request, 'Password reset email sent! Please check your inbox.')
        return redirect('home')
    return render(request, 'main/forgot_password.html')

def role_selection(request):
    return render(request, 'main/role_selection.html')

def patient(request):
    return render(request, 'main/patient.html')

def doctor(request):
    return render(request, 'main/doctor.html')

def pharmacy(request):
    return render(request, 'main/pharmacy.html')

def login_view(request):
    # Your login logic here
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')  # Redirect to a desired page after logout

def user_details(request):
    user_profile = get_object_or_404(UserProfile, user=request.user)  # Get the logged-in user's profile
    context = {
        'user_profile': user_profile,
        'medicines': user_profile.medicines.all(),
    }
    return render(request, 'main/user_details.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Perform any additional steps for registration here (e.g., creating UserProfile)
            messages.success(request, 'Registration successful.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'main/register.html', {'form': form})  # Ensure the path is correct


def user_list(request):
    # Retrieve all user profiles along with their roles and medicines
    user_profiles = UserProfile.objects.select_related('role').prefetch_related('medicines').all()

    context = {
        'user_profiles': user_profiles,
    }
    return render(request, 'main/user_list.html', context)