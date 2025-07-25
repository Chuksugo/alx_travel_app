from django.core.management.base import BaseCommand
from listings.models import Listing
import random

class Command(BaseCommand):
    help = 'Seed the database with sample listings'

    def handle(self, *args, **kwargs):
        sample_data = [
            {
                "title": "Luxury Beach House",
                "description": "A beautiful beach house with ocean views.",
                "location": "Lagos",
                "price_per_night": 200.00,
                "available": True,
            },
            {
                "title": "Mountain Cabin",
                "description": "Cozy cabin in the mountains, perfect for retreats.",
                "location": "Jos",
                "price_per_night": 150.00,
                "available": True,
            },
            {
                "title": "City Apartment",
                "description": "Modern apartment in the city center.",
                "location": "Abuja",
                "price_per_night": 100.00,
                "available": True,
            },
        ]

        for data in sample_data:
            Listing.objects.create(**data)

        self.stdout.write(self.style.SUCCESS("Successfully seeded the database with listings."))
