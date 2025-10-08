from django.core.management.base import BaseCommand
from listings.models import Listing
from django.utils import timezone
import random

class Command(BaseCommand):
    help = "Seed the database with sample listings data"

    def handle(self, *args, **kwargs):
        sample_data = [
            {
                "title": "Luxury Apartment in Lagos",
                "description": "Beautiful 2-bedroom apartment in Ikoyi with ocean view.",
                "location": "Lagos, Nigeria",
                "price_per_night": 450.00,
            },
            {
                "title": "Cozy Beach House in Lekki",
                "description": "Enjoy your stay in this cozy beachfront property.",
                "location": "Lekki, Lagos",
                "price_per_night": 350.00,
            },
            {
                "title": "Modern Duplex in Abuja",
                "description": "Spacious duplex with modern amenities in Maitama.",
                "location": "Abuja, Nigeria",
                "price_per_night": 550.00,
            },
        ]

        for data in sample_data:
            listing, created = Listing.objects.get_or_create(
                title=data["title"],
                defaults={
                    "description": data["description"],
                    "location": data["location"],
                    "price_per_night": data["price_per_night"],
                    "available": True,
                    "created_at": timezone.now(),
                },
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f"Created listing: {listing.title}"))
            else:
                self.stdout.write(self.style.WARNING(f"Listing already exists: {listing.title}"))
