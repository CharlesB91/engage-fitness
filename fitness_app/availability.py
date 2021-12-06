import datetime
from .models import Appointment


def checkAppointment(start, end):
    available_list = []
    bookingList = Appointment.objects.filter()
    for booking in bookingList:
        if booking.start > end or booking.end < start:
            available_list.append(True)
        else:
            available_list.append(False)
        return all(available_list)
