from rest_framework import serializers
from .models import Listing, Booking


class ListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Listing
        fields = ['id', 'title', 'description', 'price_per_night', 'location', 'available']


class BookingSerializer(serializers.ModelSerializer):
    listing_title = serializers.CharField(source='listing.title', read_only=True)
    
    class Meta:
        model = Booking
        fields = ['id', 'listing', 'listing_title', 'guest_name', 'check_in_date', 'check_out_date', 'total_price']
