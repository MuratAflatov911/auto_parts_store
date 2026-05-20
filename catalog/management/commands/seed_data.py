from decimal import Decimal
import random
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from catalog.models import Category, Discount, News, Product, VehicleEngine, VehicleGeneration, VehicleMake, VehicleModel


class Command(BaseCommand):
    help = 'Fill DB with realistic demo data for Automir'

    def handle(self, *args, **kwargs):
        categories = [
            'Моторные масла', 'Фильтры', 'Аккумуляторы', 'Тормозные колодки', 'Свечи зажигания',
            'Шины', 'Диски', 'Детали двигателя', 'Подвеска', 'Аксессуары', 'Ремни и ролики',
            'Тормозные диски', 'Жидкости', 'Щетки стеклоочистителя'
        ]
        cat_objs = [Category.objects.get_or_create(name=c, slug=slugify(c))[0] for c in categories]

        vehicles = {
            'LADA': {
                'Granta': ['1.6 8V 87 л.с.', '1.6 16V 98 л.с.', '1.6 16V 106 л.с.'],
                'Vesta': ['1.6 106 л.с.', '1.8 122 л.с.'],
                'Niva Travel': ['1.7 80 л.с.'],
                'XRay': ['1.6 106 л.с.', '1.8 122 л.с.'],
            },
            'ВАЗ': {
                '2107': ['1.5 карбюратор', '1.6 инжектор'],
                '2114': ['1.5 8V', '1.6 8V'],
                'Priora': ['1.6 16V 98 л.с.'],
                'Kalina': ['1.4 16V', '1.6 8V', '1.6 16V'],
            },
            'BMW': {'E34': ['2.0 бензин', '2.5 бензин'], 'E39': ['2.2 бензин', '2.5 бензин', '3.0 дизель']},
            'Mercedes-Benz': {'W124': ['2.0 бензин', '2.3 бензин', '2.5 дизель'], 'W210': ['2.0 бензин', '2.2 CDI', '3.2 бензин']},
            'Audi': {'A4 B5': ['1.6 бензин', '1.8T бензин', '1.9 TDI'], 'A6 C5': ['1.8T бензин', '2.4 бензин', '2.5 TDI']},
            'Volkswagen': {'Passat B5': ['1.6 бензин', '1.8T бензин', '1.9 TDI'], 'Polo Sedan': ['1.6 MPI 90 л.с.', '1.6 MPI 110 л.с.']},
            'Skoda': {'Octavia A5': ['1.6 MPI', '1.8 TSI', '2.0 TDI'], 'Rapid': ['1.6 MPI 90 л.с.', '1.6 MPI 110 л.с.']},
            'Toyota': {'Camry 40': ['2.4 бензин', '3.5 бензин'], 'Corolla 150': ['1.4 бензин', '1.6 бензин']},
            'Nissan': {'Almera Classic': ['1.6 бензин'], 'Qashqai J10': ['1.6 бензин', '2.0 бензин']},
            'Honda': {'Civic 4D': ['1.8 бензин'], 'CR-V III': ['2.0 бензин', '2.4 бензин']},
            'Mitsubishi': {'Lancer IX': ['1.6 бензин', '2.0 бензин'], 'Outlander XL': ['2.0 бензин', '2.4 бензин']},
            'Mazda': {'Mazda 3 BK': ['1.6 бензин', '2.0 бензин'], 'Mazda 6 GG': ['1.8 бензин', '2.0 бензин']},
            'Hyundai': {'Solaris': ['1.4 бензин', '1.6 бензин'], 'Elantra HD': ['1.6 бензин', '2.0 бензин']},
            'Kia': {'Rio': ['1.4 бензин', '1.6 бензин'], 'Ceed ED': ['1.6 бензин', '2.0 бензин']},
            'Renault': {'Logan': ['1.4 бензин', '1.6 бензин'], 'Duster': ['1.6 бензин', '2.0 бензин', '1.5 dCi']},
            'Ford': {'Focus II': ['1.6 бензин', '1.8 бензин', '2.0 бензин'], 'Mondeo IV': ['2.0 бензин', '2.3 бензин']},
            'Chevrolet': {'Lacetti': ['1.4 бензин', '1.6 бензин'], 'Cruze': ['1.6 бензин', '1.8 бензин']},
            'Opel': {'Astra H': ['1.6 бензин', '1.8 бензин'], 'Vectra C': ['1.8 бензин', '2.2 бензин']},
            'ГАЗ': {'31105': ['2.3 бензин', '2.4 бензин'], 'Газель Бизнес': ['2.7 бензин', '2.8 дизель']},
            'УАЗ': {'Патриот': ['2.7 бензин', '2.3 дизель'], 'Хантер': ['2.7 бензин']},
        }

        for make_name, models in vehicles.items():
            make = VehicleMake.objects.get_or_create(name=make_name)[0]
            for model_name, engines in models.items():
                model = VehicleModel.objects.get_or_create(make=make, name=model_name)[0]
                generation = VehicleGeneration.objects.get_or_create(model=model, name='Основное поколение')[0]
                for engine_name in engines:
                    VehicleEngine.objects.get_or_create(generation=generation, name=engine_name, year_from=1998, year_to=2021)

        product_bases = [
            ('Моторное масло Mobil 1 ESP 5W-30 4л', 'Mobil', 4250, 'Моторные масла'),
            ('Моторное масло Shell Helix Ultra 5W-40 4л', 'Shell', 4390, 'Моторные масла'),
            ('Моторное масло Лукойл Genesis Armortech 5W-40 4л', 'Лукойл', 2890, 'Моторные масла'),
            ('Фильтр масляный MANN W 914/2', 'MANN', 790, 'Фильтры'),
            ('Фильтр воздушный Bosch F026400123', 'Bosch', 990, 'Фильтры'),
            ('Фильтр салона Filtron K 1060A', 'Filtron', 820, 'Фильтры'),
            ('Аккумулятор Varta Blue Dynamic D47 60Ач', 'Varta', 9450, 'Аккумуляторы'),
            ('Колодки тормозные передние TRW GDB1330', 'TRW', 3650, 'Тормозные колодки'),
            ('Свеча зажигания NGK BKR6E-11', 'NGK', 450, 'Свечи зажигания'),
            ('Шина Cordiant Comfort 2 195/65 R15', 'Cordiant', 5800, 'Шины'),
            ('Амортизатор передний KYB Excel-G 334838', 'KYB', 5200, 'Подвеска'),
            ('Ремень ГРМ Gates K015670XS', 'Gates', 6100, 'Ремни и ролики'),
            ('Диск тормозной Brembo 09.7011.11', 'Brembo', 4700, 'Тормозные диски'),
            ('Антифриз Felix Carbox G12+ 5кг', 'Felix', 1390, 'Жидкости'),
            ('Жидкость тормозная DOT-4 RosDOT 910г', 'RosDOT', 590, 'Жидкости'),
            ('Щетка стеклоочистителя Bosch AeroTwin 600мм', 'Bosch', 1200, 'Щетки стеклоочистителя'),
            ('Лампа H7 Philips Vision +30%', 'Philips', 890, 'Аксессуары'),
            ('Стойка стабилизатора CTR CLM-9', 'CTR', 960, 'Подвеска'),
        ]

        engines = list(VehicleEngine.objects.all())
        for i in range(1, 81):
            base_name, brand, price, category_name = random.choice(product_bases)
            product, _ = Product.objects.get_or_create(
                article=f'AUT-{i:05}',
                defaults={
                    'category': Category.objects.get(name=category_name),
                    'name': base_name,
                    'slug': slugify(f'{base_name}-{i}'),
                    'description': f'{base_name}. Качественная запчасть для обслуживания и ремонта.',
                    'price': Decimal(price),
                    'old_price': Decimal(round(price * 1.15, 2)),
                    'stock': random.randint(2, 70),
                    'brand': brand,
                    'image': 'products/default_product.jpg',
                    'is_popular': i % 4 == 0,
                }
            )
            product.compatible_engines.set(random.sample(engines, k=min(12, len(engines))))

        Discount.objects.get_or_create(
            title='Скидка на ТО комплект',
            defaults={'description': 'До -20% на масло + фильтры + свечи.', 'percent': 20, 'active': True}
        )
        News.objects.get_or_create(
            title='Новая поставка запчастей для популярных моделей',
            defaults={'content': 'В наличии товары для LADA, Toyota, VW, Kia, Hyundai, BMW и др.'}
        )
        self.stdout.write(self.style.SUCCESS('Demo data created: realistic vehicles and 80 products.'))
