from django.contrib import admin
from .models import Listing, Booking, Review


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['title', 'location', 'price_per_night', 'available']
    list_filter = ['available', 'location']
    search_fields = ['title', 'location', 'description']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['guest_name', 'listing', 'check_in_date', 'check_out_date', 'total_price']
    list_filter = ['check_in_date', 'check_out_date']
    search_fields = ['guest_name', 'listing__title']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['reviewer_name', 'listing', 'rating']
    list_filter = ['rating']
    search_fields = ['reviewer_name', 'listing__title', 'comment']
