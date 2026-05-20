# Дипломный проект: Интернет-магазин автозапчастей «Автомир»

## Запуск в PyCharm
1. **Откройте проект**: `File -> Open` и выберите папку `auto_parts_store`.
2. **Создайте venv**: `Settings -> Project -> Python Interpreter -> Add -> Virtualenv`.
3. **Установите зависимости**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Миграции**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. **Создайте суперпользователя**:
   ```bash
   python manage.py createsuperuser
   ```
6. **Заполните тестовыми данными**:
   ```bash
   python manage.py seed_data
   ```
7. **Запуск**:
   ```bash
   python manage.py runserver
   ```

## Приложения
- `main` — главная, о компании, контакты, новости, акции, 404/500.
- `catalog` — категории, товары, фильтрация, карточка товара, подбор авто.
- `accounts` — регистрация, авторизация, личный кабинет.
- `cart` — корзина.
- `orders` — оформление заказа.
- `reviews` — отзывы.
