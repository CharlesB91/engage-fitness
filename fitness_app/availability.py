import datetime
from .models import Appointment


def checkAppointment(start, end):
    available_list = []
    bookingList = Appointment.objects.filter()
    for booking in bookingList:
        if booking.start == start and booking.end == end:
            available_list.append(True)
            print("Cant be booked")
        else:
            available_list.append(False)
            print("Cann be booked")
        return all(available_list)

