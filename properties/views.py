from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth

from messaging.models import Notification
from bookings.models import Booking

from .models import Property, PropertyImage, EmailOTP
from .forms import PropertyForm

import random
from django.core.mail import send_mail

# IMPORTANT (custom user model)
from users.models import User



# =====================
# HOME
# =====================

def home(request):

    properties = Property.objects.all()

    return render(request, 'home.html', {'properties': properties})



# =====================
# PROPERTY LIST
# =====================

def property_list(request):

    location = request.GET.get('location')

    if location:
        properties = Property.objects.filter(location__icontains=location)
    else:
        properties = Property.objects.all()

    return render(request, 'property_list.html', {'properties': properties})



# =====================
# PROPERTY DETAIL
# =====================

def property_detail(request, id):

    property = get_object_or_404(Property, id=id)

    return render(request, 'property_detail.html', {'property': property})



# =====================
# BOOKING
# =====================

@login_required
def booking_page(request, id):

    property = get_object_or_404(Property, id=id)

    if request.method == "POST":

        check_in = request.POST.get('check_in')
        check_out = request.POST.get('check_out')

        booking = Booking.objects.create(
            property=property,
            guest=request.user,
            check_in=check_in,
            check_out=check_out,
            total_price=property.price_per_night,
            booking_status="pending"
        )

        Notification.objects.create(
            user=property.host,
            message=f"New booking request from {request.user.username} for {property.title}"
        )

        return redirect('booking_success', booking.id)

    return render(request, 'booking.html', {'property': property})



# =====================
# HOST DASHBOARD
# =====================

@login_required
def host_dashboard(request):

    properties = Property.objects.filter(host=request.user)

    bookings = Booking.objects.filter(property__host=request.user)

    total_properties = properties.count()

    total_bookings = bookings.count()

    total_earnings = bookings.aggregate(
        total=Sum('total_price')
    )['total'] or 0


    revenue_data = (
        bookings
        .annotate(month=TruncMonth('created_at'))
        .values('month')
        .annotate(total=Sum('total_price'))
        .order_by('month')
    )

    months = []
    revenue = []

    for data in revenue_data:
        months.append(data['month'].strftime("%b"))
        revenue.append(float(data['total']))


    booking_data = (
        bookings
        .annotate(month=TruncMonth('created_at'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )

    booking_counts = []

    for data in booking_data:
        booking_counts.append(data['count'])


    context = {
        "properties": properties,
        "total_properties": total_properties,
        "total_bookings": total_bookings,
        "total_earnings": total_earnings,
        "months": months,
        "revenue": revenue,
        "booking_counts": booking_counts
    }

    return render(request, "host_dashboard.html", context)



# =====================
# ADD PROPERTY
# =====================

@login_required
def add_property(request):

    if request.method == "POST":

        form = PropertyForm(request.POST)

        if form.is_valid():

            property = form.save(commit=False)

            property.host = request.user

            property.save()

            return redirect('/host-dashboard')

    else:

        form = PropertyForm()

    return render(request, 'add_property.html', {'form': form})



# =====================
# EDIT PROPERTY
# =====================

@login_required
def edit_property(request, id):

    property = get_object_or_404(Property, id=id)

    form = PropertyForm(instance=property)

    if request.method == "POST":

        form = PropertyForm(request.POST, instance=property)

        if form.is_valid():

            form.save()

            return redirect('/host-dashboard')

    return render(request, 'edit_property.html', {'form': form})



# =====================
# DELETE PROPERTY
# =====================

@login_required
def delete_property(request, id):

    property = get_object_or_404(Property, id=id)

    property.delete()

    return redirect('/host-dashboard')



# =====================
# UPLOAD IMAGE
# =====================

@login_required
def upload_image(request, id):

    property = get_object_or_404(Property, id=id)

    if request.method == "POST":

        image = request.FILES.get('image')

        PropertyImage.objects.create(
            property=property,
            image=image
        )

        return redirect('/host-dashboard')

    return render(request, 'upload_image.html', {'property': property})



# =====================
# REGISTER WITH OTP
# =====================

def register(request):

    if request.method == "POST":

        username = request.POST.get("username")

        email = request.POST.get("email")

        password = request.POST.get("password")


        otp = str(random.randint(100000,999999))


        EmailOTP.objects.create(

            email=email,

            otp=otp

        )


        send_mail(

            "OTP Verification",

            f"Your OTP is {otp}",

            "yourgmail@gmail.com",

            [email],

            fail_silently=False,

        )


        request.session['username'] = username

        request.session['email'] = email

        request.session['password'] = password


        return redirect('verify_otp')


    return render(request,'register.html')



# =====================
# VERIFY OTP
# =====================

def verify_otp(request):

    if request.method == "POST":

        entered_otp = request.POST.get("otp")

        email = request.session.get('email')


        otp_obj = EmailOTP.objects.filter(email=email).last()


        if otp_obj and otp_obj.otp == entered_otp:


            User.objects.create_user(

                username=request.session.get('username'),

                email=email,

                password=request.session.get('password')

            )


            otp_obj.delete()


            return redirect('login')


        else:


            return render(

                request,

                'verify_otp.html',

                {'error':'Invalid OTP'}

            )


    return render(request,'verify_otp.html')