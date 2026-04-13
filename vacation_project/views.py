from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from django.contrib.auth.decorators import login_required
from bookings.models import Booking


@login_required
def download_booking_pdf(request, booking_id):

    booking = Booking.objects.get(id=booking_id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="booking_{booking.id}.pdf"'

    doc = SimpleDocTemplate(response)

    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("Booking Details", styles['Title']))
    elements.append(Spacer(1,12))

    elements.append(Paragraph(f"User: {booking.user}", styles['Normal']))
    elements.append(Paragraph(f"Property: {booking.property.title}", styles['Normal']))
    elements.append(Paragraph(f"Check-in: {booking.check_in}", styles['Normal']))
    elements.append(Paragraph(f"Check-out: {booking.check_out}", styles['Normal']))
    elements.append(Paragraph(f"Price: ₹{booking.price}", styles['Normal']))

    doc.build(elements)

    return response

