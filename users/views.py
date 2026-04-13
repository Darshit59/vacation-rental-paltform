from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from bookings.models import Booking

User = get_user_model()


# Register
def register_user(request):

    if request.method == "POST":

        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect('/login')

    return render(request, 'register.html')


# Login
def login_user(request):

    if request.method == "POST":

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')

    return render(request, 'login.html')


# Logout
def logout_user(request):

    logout(request)

    return redirect('/')


# User Dashboard
@login_required
def dashboard(request):

    bookings = Booking.objects.filter(guest=request.user)

    return render(request, 'dashboard.html', {'bookings': bookings})


# User Profile
@login_required
def profile(request):

    user = request.user

    if request.method == "POST":

        user.username = request.POST.get('username')
        user.email = request.POST.get('email')
        user.phone = request.POST.get('phone')

        if request.FILES.get('profile_image'):
            user.profile_image = request.FILES.get('profile_image')

        user.save()

    return render(request, 'profile.html', {'user': user})