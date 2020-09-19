from django.contrib import admin
from busapp.models import Busbooking,Welcome_Form
class BookingAdmin(admin.ModelAdmin):
    '''
        Admin View for Booking_details
    '''
    list_display = ('NAME','EMAIL','PH_NO')

admin.site.register(Busbooking, BookingAdmin)

class WelcomeAdmin(admin.ModelAdmin):
    '''
        Admin View for Welcome
    '''
    list_display = ('FROM','TO','BUSNAME','BUSTIME')

admin.site.register(Welcome_Form, WelcomeAdmin)