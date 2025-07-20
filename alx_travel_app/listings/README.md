# Listings App

The **Listings** app is the core component of the ALX Travel App that manages property listings for the travel booking platform. This Django app provides models, serializers, views, and API endpoints for handling property listings, their associated bookings, and reviews.

## Overview

The Listings app handles:
- **Property Listings**: Create, read, update, and delete property listings
- **Bookings Management**: Handle reservations for listed properties
- **Reviews System**: Manage customer reviews and ratings for properties
- **RESTful API**: Expose endpoints for frontend consumption
- **Data Management**: Admin interface and database operations

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

The Listings app exposes the following REST API endpoints:

### Listings Endpoints
- `GET /api/listings/` - Retrieve all property listings
- `POST /api/listings/` - Create a new property listing
- `GET /api/listings/{id}/` - Retrieve a specific listing
- `PUT /api/listings/{id}/` - Update a specific listing
- `PATCH /api/listings/{id}/` - Partially update a listing
- `DELETE /api/listings/{id}/` - Delete a listing

### Bookings Endpoints
- `GET /api/bookings/` - Retrieve all bookings
- `POST /api/bookings/` - Create a new booking
- `GET /api/bookings/{id}/` - Retrieve a specific booking
- `PUT /api/bookings/{id}/` - Update a booking
- `DELETE /api/bookings/{id}/` - Cancel a booking

### Documentation
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

## App Structure

```
listings/                   # Listings Django App
├── __init__.py            # Python package marker
├── admin.py               # Django admin configuration
├── apps.py                # App configuration
├── models.py              # Database models (Listing, Booking, Review)
├── serializers.py         # DRF serializers for API data
├── views.py               # API views and business logic
├── urls.py                # URL patterns for the app
├── tests.py               # Unit tests (if any)
├── management/            # Custom management commands
│   ├── __init__.py
│   └── commands/
│       ├── __init__.py
│       └── seed.py        # Database seeding command
├── migrations/            # Database migration files
│   ├── __init__.py
│   ├── 0001_initial.py    # Initial migration
│   └── ...                # Additional migrations
└── README.md              # This documentation file
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

### Core Functionality
- ✅ **Listing Management**: Full CRUD operations for property listings
- ✅ **Booking System**: Create and manage reservations for properties
- ✅ **Review System**: Customer reviews and ratings for listings
- ✅ **Availability Tracking**: Monitor property availability status

### Technical Features
- ✅ **REST API**: Full CRUD operations via Django REST Framework
- ✅ **Data Serialization**: Proper JSON serialization for all models
- ✅ **Database Relations**: Foreign key relationships between models
- ✅ **Database Seeding**: Automated sample data generation via management command
- ✅ **Admin Interface**: Django admin integration for easy data management
- ✅ **API Documentation**: Auto-generated Swagger/ReDoc documentation
- ✅ **Input Validation**: Model-level and serializer-level data validation

## Development

To extend the application:
1. Add new models in `listings/models.py`
2. Create corresponding serializers in `listings/serializers.py`
3. Implement views in `listings/views.py`
4. Update URL patterns in `listings/urls.py`
5. Run migrations: `python manage.py makemigrations && python manage.py migrate`

## License

This project is created for educational purposes as part of the ALX Software Engineering program.
