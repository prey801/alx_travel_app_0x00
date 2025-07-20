# ALX Travel App 0x00

A Django REST API application for managing travel listings, bookings, and reviews.

## Project Overview

This project implements a travel booking system with the following key features:
- Property listings management
- Booking system for reservations
- Review and rating system
- RESTful API endpoints for data access
- Database seeding with sample data

## Models

### Listing
Represents a property available for booking.
- `title`: Property title (CharField, max_length=255)
- `description`: Detailed property description (TextField)
- `price_per_night`: Nightly rate (DecimalField)
- `location`: Property location (CharField, max_length=255)
- `available`: Availability status (BooleanField, default=True)

### Booking
Represents a reservation for a listing.
- `listing`: Foreign key to Listing model
- `guest_name`: Name of the guest (CharField, max_length=255)
- `check_in_date`: Check-in date (DateField)
- `check_out_date`: Check-out date (DateField)
- `total_price`: Total booking cost (DecimalField)

### Review
Represents a review for a listing.
- `listing`: Foreign key to Listing model
- `reviewer_name`: Name of the reviewer (CharField, max_length=255)
- `rating`: Rating score (IntegerField)
- `comment`: Review comment (TextField)

## API Endpoints

The application provides REST API endpoints for:
- Listings management (`/api/listings/`)
- Bookings management (`/api/bookings/`)
- API documentation (`/swagger/` and `/redoc/`)

## Setup Instructions

1. **Install Dependencies**
   ```bash
   pip install django djangorestframework django-cors-headers drf-yasg django-environ
   ```

2. **Database Setup**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

3. **Seed Database with Sample Data**
   ```bash
   python manage.py seed
   ```

4. **Create Superuser (Optional)**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

## Database Seeding

The project includes a management command to populate the database with sample data:

```bash
python manage.py seed
```

This command creates:
- 5 sample property listings (apartments, villas, cabins, etc.)
- Multiple bookings with realistic date ranges
- Customer reviews with ratings and comments

## API Documentation

Once the server is running, you can access:
- Swagger UI: `http://localhost:8000/swagger/`
- ReDoc: `http://localhost:8000/redoc/`
- Django Admin: `http://localhost:8000/admin/`

## File Structure

```
alx_travel_app_0x00/
├── alx_travel_app/          # Project configuration
│   ├── settings.py          # Django settings
│   ├── urls.py             # Main URL configuration
│   └── ...
├── listings/               # Main application
│   ├── models.py           # Database models
│   ├── serializers.py      # DRF serializers
│   ├── views.py            # API views
│   ├── urls.py             # App URLs
│   ├── admin.py            # Django admin config
│   ├── management/
│   │   └── commands/
│   │       └── seed.py     # Database seeding command
│   └── migrations/         # Database migrations
├── manage.py               # Django management script
└── README.md              # This file
```

## Technologies Used

- **Django 5.1.4**: Web framework
- **Django REST Framework**: API development
- **SQLite**: Database (default, can be configured for MySQL)
- **django-cors-headers**: CORS handling
- **drf-yasg**: API documentation
- **django-environ**: Environment variable management

## Environment Configuration

The project supports both SQLite (default) and MySQL databases. Configure via environment variables in `.env` file:

```env
MYSQL_DATABASE=your_database_name
MYSQL_USER=your_username
MYSQL_PASSWORD=your_password
MYSQL_HOST=localhost
MYSQL_PORT=3306
```

## Features

- ✅ **Database Models**: Comprehensive models for listings, bookings, and reviews
- ✅ **REST API**: Full CRUD operations via DRF
- ✅ **Data Serialization**: Proper API data representation
- ✅ **Database Seeding**: Automated sample data generation
- ✅ **Admin Interface**: Django admin for data management
- ✅ **API Documentation**: Swagger/ReDoc integration
- ✅ **CORS Support**: Cross-origin request handling

## Development

To extend the application:
1. Add new models in `listings/models.py`
2. Create corresponding serializers in `listings/serializers.py`
3. Implement views in `listings/views.py`
4. Update URL patterns in `listings/urls.py`
5. Run migrations: `python manage.py makemigrations && python manage.py migrate`

## License

This project is created for educational purposes as part of the ALX Software Engineering program.
