from decimal import Decimal
import random
from django.core.management.base import BaseCommand
from django.utils.text import slugify
from catalog.models import (
    Category, Discount, News, Product, VehicleEngine,
    VehicleGeneration, VehicleMake, VehicleModel,
)


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
            'LADA': ['Vesta', 'XRay', 'Niva Travel', 'Granta'],
            'ВАЗ': ['2107', '2110', '2114', 'Priora', 'Kalina'],
            'ГАЗ': ['31105', 'Газель Бизнес'],
            'УАЗ': ['Патриот', 'Хантер'],
            'BMW': ['E34', 'E39', 'E46', 'X5 E53'],
            'Mercedes-Benz': ['W124', 'W210', 'W211', 'C204'],
            'Audi': ['80 B4', 'A4 B5', 'A6 C4', 'A6 C5'],
            'Volkswagen': ['Passat B5', 'Golf IV', 'Polo Sedan'],
            'Skoda': ['Octavia A5', 'Rapid', 'Fabia'],
            'Toyota': ['Camry 40', 'Camry 50', 'Corolla 120', 'Corolla 150'],
            'Nissan': ['Almera Classic', 'Qashqai J10', 'X-Trail T31'],
            'Honda': ['Civic 4D', 'CR-V III'],
            'Mitsubishi': ['Lancer IX', 'Outlander XL'],
            'Mazda': ['Mazda 3 BK', 'Mazda 6 GG'],
            'Hyundai': ['Solaris', 'Elantra HD', 'Santa Fe CM'],
            'Kia': ['Rio', 'Ceed ED', 'Sportage III'],
            'Renault': ['Logan', 'Duster', 'Megane II'],
            'Ford': ['Focus II', 'Mondeo IV'],
            'Chevrolet': ['Lacetti', 'Cruze', 'Niva'],
            'Opel': ['Astra H', 'Vectra C', 'Zafira B'],
        }
        engine_pool = [
            ('1.4 бензин', 1.4), ('1.6 бензин', 1.6), ('1.8 бензин', 1.8), ('2.0 бензин', 2.0),
            ('2.0 дизель', 2.0), ('2.5 бензин', 2.5), ('3.0 дизель', 3.0)
        ]

        for make_name, models in vehicles.items():
            make = VehicleMake.objects.get_or_create(name=make_name)[0]
            for model_name in models:
                model = VehicleModel.objects.get_or_create(make=make, name=model_name)[0]
                for gen_name in ['I', 'II']:
                    gen = VehicleGeneration.objects.get_or_create(model=model, name=gen_name)[0]
                    for eng_name, volume in random.sample(engine_pool, k=3):
                        VehicleEngine.objects.get_or_create(
                            generation=gen, name=eng_name, volume=str(volume), year_from=1998, year_to=2016
                        )

        products = [
            ('Моторное масло Mobil 1 ESP 5W-30 4л', 'Mobil', 4250),
            ('Моторное масло Лукойл Genesis Armortech 5W-40 4л', 'Лукойл', 2890),
            ('Фильтр масляный MANN W 914/2', 'MANN', 790),
            ('Фильтр воздушный Bosch F026400123', 'Bosch', 990),
            ('Аккумулятор Varta Blue Dynamic D47 60Ач', 'Varta', 9450),
            ('Колодки тормозные передние TRW GDB1330', 'TRW', 3650),
            ('Свеча зажигания NGK BKR6E-11', 'NGK', 450),
            ('Шина Cordiant Comfort 2 195/65 R15', 'Cordiant', 5800),
            ('Диск литой K&K КС699 6.5x16 5x114.3', 'K&K', 7450),
            ('Амортизатор передний KYB Excel-G 334838', 'KYB', 5200),
            ('Ремень ГРМ Gates K015670XS', 'Gates', 6100),
            ('Помпа водяная Hepu P673', 'Hepu', 4350),
            ('Диск тормозной Brembo 09.7011.11', 'Brembo', 4700),
            ('Фильтр салонный угольный Filtron K 1060A', 'Filtron', 820),
            ('Антифриз Felix Carbox G12+ 5кг', 'Felix', 1390),
            ('Жидкость тормозная DOT-4 RosDOT 910г', 'RosDOT', 590),
            ('Щетка стеклоочистителя Bosch AeroTwin 600мм', 'Bosch', 1200),
            ('Лампа H7 Philips Vision +30%', 'Philips', 890),
            ('Стойка стабилизатора CTR CLM-9', 'CTR', 960),
            ('Опора двигателя Lemforder 34756 01', 'Lemforder', 3800),
        ]

        engines = list(VehicleEngine.objects.all())
        for i in range(1, 61):
            base_name, brand, price = random.choice(products)
            name = f'{base_name} (партия {i})'
            product, _ = Product.objects.get_or_create(
                slug=slugify(f'{name}-{i}'),
                defaults={
                    'category': random.choice(cat_objs),
                    'name': name,
                    'description': f'{name}. Оригинальное качество, гарантия, подходит для регулярного ТО.',
                    'price': Decimal(price),
                    'old_price': Decimal(round(price * 1.18, 2)),
                    'stock': random.randint(2, 70),
                    'article': f'AUT-{i:05}',
                    'brand': brand,
                    'image': 'products/default_product.jpg',
                    'is_popular': i % 4 == 0,
                }
            )
            product.compatible_engines.set(random.sample(engines, k=min(10, len(engines))))

        Discount.objects.get_or_create(
            title='Скидка на ТО комплект',
            defaults={'description': 'До -20% на масло + фильтры + свечи.', 'percent': 20, 'active': True}
        )
        News.objects.get_or_create(
            title='Новая поставка запчастей для LADA, Toyota и Volkswagen',
            defaults={'content': 'Поступили популярные позиции для ТО и ремонта подвески.'}
        )

        self.stdout.write(self.style.SUCCESS('Demo data created: vehicles, 60 products, discounts, news.'))
