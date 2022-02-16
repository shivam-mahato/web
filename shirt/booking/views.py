from django.shortcuts import redirect, render
from booking.forms import BookingForm
from booking.models import Booking

from shirtsapp.models import Decoration

# Create your views here.

def bookingnew(request,id):
    decoration = Decoration.objects.get(id=id)
    return render(request,'booking/booking_new.html',{'decoration':decoration})
    
def bookingfinal(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        print(form)
        print("valid")
        form.save()
        return redirect("/")
                
def bookingview(request):
    bookings = Booking.objects.all()
    return render(request,'booking/bookingview.html',{'bookings':bookings})
         
