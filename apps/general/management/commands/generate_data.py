import os
import random

from faker import Faker
from datetime import datetime, timedelta

from django.db import transaction
from django.conf import settings
from django.utils.timezone import now
from django.core.management import BaseCommand

from apps.categories.models import Category

from apps.general.management.commands.service import random_image_download
from apps.products.models import Product

fake = Faker()
brands = [
    'nexatech solutions', 'zenith digital', 'cloudnova systems', 'cybersphere', 'quantumedge',
    'titan motors', 'velocity autoworks', 'ignite motors', 'infinity rides', 'urbandrive',
    'code catalyst', 'binary bliss', 'quantum quorum', 'pixel pioneers', 'silicon surge',
    'circuit cipher', 'data dynamics', 'alpha algorithm', 'techno tetra', 'digit dimension',
    'cyber cascade', 'nano nexus', 'quantum quill', 'optic oracle', 'virtual velocity',
    'cybercore', 'bytebridge', 'codehive', 'techlynx', 'digitalwaves',
    'toyota', 'honda', 'ford', 'chevrolet', 'nissan', 'bmw', 'mercedes-benz', 'audi',
    'volkswagen', 'hyundai', 'kia', 'subaru', 'mazda', 'lexus', 'jeep', 'dodge', 'ram',
    'gmc', 'tesla', 'volvo', 'land rover', 'jaguar', 'porsche', 'ferrari', 'lamborghini',
    'maserati', 'alfa romeo', 'fiat', 'peugeot', 'citroën', 'renault', 'skoda', 'seat',
    'opel', 'vauxhall', 'suzuki', 'mitsubishi', 'isuzu', 'daihatsu', 'chery', 'geely', 'byd',
    'great wall motors', 'tata motors', 'mahindra', 'proton', 'perodua', 'ssangyong', 'daewoo',
    'holden', 'scion', 'hummer', 'saturn', 'pontiac', 'saab'
]
colors = [
    'red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'black', 'white',
    'gray', 'cyan', 'magenta', 'lime', 'maroon', 'navy', 'olive', 'teal', 'aqua', 'silver',
    'gold', 'beige', 'coral', 'crimson', 'darkgreen', 'darkblue', 'darkred', 'indigo', 'ivory',
    'khaki', 'lavender', 'lightblue', 'lightgreen', 'limegreen', 'mint', 'mustard', 'navyblue',
    'orchid', 'peach', 'plum', 'salmon', 'sienna', 'tan', 'turquoise', 'violet', 'wheat',
    'chartreuse', 'chocolate', 'emerald', 'fuchsia'
]

def random_date(start, end):
    delta = end - start
    random_seconds = random.randint(0, int(delta.total_seconds()))
    return start + timedelta(seconds=random_seconds)

start_date = datetime(2020, 1, 1)
end_date = datetime.now()
random_created_at = random_date(start_date, end_date)


class Command(BaseCommand):

    @staticmethod
    def generate_products():
        today = now().date()
        django_filename = f'products/images/{today.year}/{today.month}/{today.day}/'
        image_dir = os.path.join(settings.MEDIA_ROOT, django_filename)

        for cat_i in range(10):
            image_name = random_image_download(image_dir)
            category = Category.objects.create(
                name=fake.first_name(),
                image=os.path.join(django_filename, image_name),
                is_active=random.choice([True, False]),

            )


            #============children Category===========
            if cat_i %2 :
                for i in range(3):
                    Category.objects.create(
                        name=fake.last_name(),
                        parent_id=category.pk,
                    )


            products = []
            counts = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
            print(f'Please, Wait for {len(counts) - cat_i} seconds !\n')
            if cat_i + 1 == 1:
                print(f'\t{cat_i + 1} category created ! {(cat_i + 1) * 100} products created !\n')
            else:
                print(f'\t{cat_i + 1} categories created ! {(cat_i + 1) * 100} products created !\n')

            for pro_i in range(100):
                if cat_i in counts:
                    counts.remove(cat_i)
                products.append(
                    Product(
                        title=fake.text(50),
                        name=fake.name(),
                        short_description=fake.text(255),
                        long_description=fake.text(500),
                        category_id=category.pk,
                        image=os.path.join(django_filename, image_name),
                        price=random.randint(100, 100000),
                        discount_price=random.randint(99, 99999),
                        stock=random.randint(1, 10000),
                        is_active=random.choice([True, False]),
                        is_featured=random.choice([True, False]),
                        brand=random.choice(brands),
                        rating=random.randint(0,5),
                        num_reviews=random.randint(0, 100),
                        color=random.choice(colors),
                        size=random.randint(12, 99),
                        weight=random.randint(0,100),
                        created_at=random_created_at,
                        updated_at=random_created_at,
                    )
                )
            Product.objects.bulk_create(products)

    @transaction.atomic
    def handle(self, *args, **options):
        # ====================== generate product model ======================
        print(self.stdout.write(self.style.SUCCESS('Successfully generated products data')))
        self.generate_products()
        print(self.stdout.write(self.style.SUCCESS('Done')))
