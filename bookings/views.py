from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

from .models import Booking


@login_required
def host_bookings(request):

    bookings = Booking.objects.filter(property__host=request.user)

    return render(request, 'host_bookings.html', {'bookings': bookings})


@login_required
def approve_booking(request, id):

    booking = Booking.objects.get(id=id)
    booking.booking_status = "confirmed"
    booking.save()

    return redirect('/host-bookings/')


@login_required
def reject_booking(request, id):

    booking = Booking.objects.get(id=id)
    booking.booking_status = "cancelled"
    booking.save()

    return redirect('/host-bookings/')


def booking_success(request, booking_id):

    booking = get_object_or_404(Booking, id=booking_id)

    return render(
        request,
        "booking_success.html",
        {"booking": booking}
    )


# PDF download function
def download_booking_pdf(request, booking_id):

    booking = get_object_or_404(Booking, id=booking_id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="booking_{booking.id}.pdf"'

    doc = SimpleDocTemplate(response)

    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Booking Details", styles['Title']))
    elements.append(Spacer(1,12))

    elements.append(Paragraph(f"Property: {booking.property.title}", styles['Normal']))
    elements.append(Paragraph(f"Guest: {booking.guest.username}", styles['Normal']))
    elements.append(Paragraph(f"Check-in: {booking.check_in}", styles['Normal']))
    elements.append(Paragraph(f"Check-out: {booking.check_out}", styles['Normal']))
    elements.append(Paragraph(f"Total Price: ₹{booking.total_price}", styles['Normal']))
    elements.append(Paragraph(f"Status: {booking.booking_status}", styles['Normal']))

    doc.build(elements)

    return response