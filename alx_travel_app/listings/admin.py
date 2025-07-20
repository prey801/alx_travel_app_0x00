from django.contrib import admin
from .models import Listing, Booking, Review


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'price_per_night', 'host']
    list_filter = ['location', 'created_at']
    search_fields = ['name', 'location', 'description']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['guest', 'listing', 'start_date', 'end_date', 'total_price', 'status']
    list_filter = ['start_date', 'end_date', 'status']
    search_fields = ['guest__username', 'listing__name']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['guest', 'listing', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['guest__username', 'listing__name', 'comment']
