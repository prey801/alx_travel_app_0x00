from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
from decimal import Decimal
import random
from datetime import date, timedelta


class Command(BaseCommand):
    help = 'Seed the database with sample listings data'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Starting database seeding...'))
        
        # Clear existing data
        Listing.objects.all().delete()
        Booking.objects.all().delete()
        Review.objects.all().delete()
        
        # Sample listings data
        listings_data = [
            {
                'title': 'Cozy Apartment in Downtown',
                'description': 'A beautiful and cozy apartment located in the heart of downtown. Perfect for business travelers and tourists alike.',
                'price_per_night': Decimal('120.00'),
                'location': 'New York, NY',
                'available': True
            },
            {
                'title': 'Beachfront Villa',
                'description': 'Stunning beachfront villa with ocean views. Includes private beach access and modern amenities.',
                'price_per_night': Decimal('350.00'),
                'location': 'Miami Beach, FL',
                'available': True
            },
            {
                'title': 'Mountain Cabin Retreat',
                'description': 'Peaceful cabin in the mountains. Perfect for nature lovers and those seeking a quiet getaway.',
                'price_per_night': Decimal('200.00'),
                'location': 'Aspen, CO',
                'available': True
            },
            {
                'title': 'Modern Loft in Tech District',
                'description': 'Contemporary loft in the bustling tech district. High-speed internet and modern workspace included.',
                'price_per_night': Decimal('180.00'),
                'location': 'San Francisco, CA',
                'available': True
            },
            {
                'title': 'Historic Townhouse',
                'description': 'Charming historic townhouse with original architecture and modern updates. Walking distance to major attractions.',
                'price_per_night': Decimal('250.00'),
                'location': 'Boston, MA',
                'available': True
            }
        ]
        
        # Create listings
        created_listings = []
        for listing_data in listings_data:
            listing = Listing.objects.create(**listing_data)
            created_listings.append(listing)
            self.stdout.write(f'Created listing: {listing.title}')
        
        # Create sample bookings
        guest_names = ['John Smith', 'Jane Doe', 'Alice Johnson', 'Bob Wilson', 'Carol Brown']
        for i, listing in enumerate(created_listings):
            # Create 1-2 bookings per listing
            for j in range(random.randint(1, 2)):
                check_in = date.today() + timedelta(days=random.randint(30, 90))
                check_out = check_in + timedelta(days=random.randint(2, 7))
                nights = (check_out - check_in).days
                total_price = listing.price_per_night * nights
                
                booking = Booking.objects.create(
                    listing=listing,
                    guest_name=random.choice(guest_names),
                    check_in_date=check_in,
                    check_out_date=check_out,
                    total_price=total_price
                )
                self.stdout.write(f'Created booking: {booking}')
        
        # Create sample reviews
        reviewers = ['Mike Davis', 'Sarah Wilson', 'Tom Anderson', 'Lisa Garcia', 'David Miller']
        review_comments = [
            'Amazing place! Would definitely stay again.',
            'Great location and very clean. Highly recommended.',
            'Perfect for our vacation. Host was very responsive.',
            'Beautiful property with excellent amenities.',
            'Good value for money. Enjoyed our stay.',
            'Exceeded our expectations in every way.',
            'Comfortable and well-equipped. Great experience.'
        ]
        
        for listing in created_listings:
            # Create 1-3 reviews per listing
            for j in range(random.randint(1, 3)):
                review = Review.objects.create(
                    listing=listing,
                    reviewer_name=random.choice(reviewers),
                    rating=random.randint(3, 5),
                    comment=random.choice(review_comments)
                )
                self.stdout.write(f'Created review: {review}')
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully seeded database with {len(created_listings)} listings, '
                f'{Booking.objects.count()} bookings, and {Review.objects.count()} reviews'
            )
        )
