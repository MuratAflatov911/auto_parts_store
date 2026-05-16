from django.core.management.base import BaseCommand
from django.utils.text import slugify
from catalog.models import *
import random
class Command(BaseCommand):
    def handle(self,*args,**kwargs):
        cats=['Моторные масла','Фильтры','Аккумуляторы','Тормозные колодки','Свечи зажигания','Шины','Диски','Детали двигателя','Подвеска','Аксессуары']
        c_objs=[Category.objects.get_or_create(name=c,slug=slugify(c))[0] for c in cats]
        makes={'ВАЗ':['2107','2114','Priora','Granta'],'BMW':['E34','E39'],'Mercedes-Benz':['W124','W210'],'Audi':['C4','A4 B5'],'Volkswagen':['Passat B5','Golf 4'],'Toyota':['Camry 40','Corolla'],'Hyundai':['Solaris'],'Kia':['Rio']}
        engines=['1.6 бензин','2.0 бензин','2.5 бензин','2.0 дизель']
        for make,models in makes.items():
            mk=VehicleMake.objects.get_or_create(name=make)[0]
            for m in models:
                md=VehicleModel.objects.get_or_create(make=mk,name=m)[0]; gen=VehicleGeneration.objects.get_or_create(model=md,name='I')[0]
                for e in engines: VehicleEngine.objects.get_or_create(generation=gen,name=e,year_from=1995,year_to=2010)
        engs=list(VehicleEngine.objects.all())
        brands=['Lukoil','Mann','Bosch','NGK','Sakura','Mobil']
        for i in range(1,31):
            p,_=Product.objects.get_or_create(slug=f'product-{i}',defaults=dict(category=random.choice(c_objs),name=f'Запчасть {i}',description='Качественная автозапчасть для регулярного ТО и ремонта.',price=random.randint(800,12000),old_price=random.randint(1300,15000),stock=random.randint(1,40),article=f'ART-{i:04}',brand=random.choice(brands),is_popular=i%3==0))
            p.compatible_engines.set(random.sample(engs,k=min(5,len(engs))))
        Discount.objects.get_or_create(title='Весенняя скидка',defaults={'description':'Скидки на расходники до конца месяца','percent':15,'active':True})
        News.objects.get_or_create(title='Открытие нового пункта выдачи в Апшеронске',defaults={'content':'Мы расширили географию выдачи заказов.'})
        self.stdout.write(self.style.SUCCESS('Test data created'))
