from datetime import date

# ===== 1. ПРОСТЫЕ ТИПЫ ДАННЫХ =====
# Сущность: Пользователь
client_name = "Иванов Иван Иванович"
client_phone = "+79991234567"

# Сущность: Автомобиль
car_model = "Kia Rio"
car_license_plate = "Е777ОУ777"

# Сущность: Парковочное место
parking_spot_id = 15
is_spot_covered = True
is_spot_available = True

# ===== 2. ИМПОРТИРУЕМЫЕ ТИПЫ ДАННЫХ =====
# Сущность: Период бронирования
booking_start = date(2026, 9, 20)
booking_end = date(2026, 9, 25)

# ===== 3. ОПЕРАЦИИ И ПРЕОБРАЗОВАНИЕ ТИПОВ =====
daily_rate = 450.75
booking_days = (booking_end - booking_start).days
total_price_float = booking_days * daily_rate
total_price_int = int(total_price_float)  # преобразование float -> int

# ===== 4. ВЕТВЛЕНИЯ (if/elif/else) =====
if not is_spot_available:
    print("❌ Ошибка: Выбранное парковочное место уже занято.")
elif booking_days <= 0:
    print("❌ Ошибка: Неверно указан период бронирования.")
else:
    if is_spot_covered:
        spot_type_str = "Крытое"
    else:
        spot_type_str = "Открытое"

    print("=" * 45)
    print("  ЧЕК БРОНИРОВАНИЯ ПАРКОВОЧНОГО МЕСТА")
    print("=" * 45)
    print(f"Клиент: {client_name}")
    print(f"Телефон: {client_phone}")
    print(f"Автомобиль: {car_model} ({car_license_plate})")
    print(f"Место № {parking_spot_id} ({spot_type_str})")
    print(f"Период: с {booking_start} по {booking_end}")
    print(f"Количество дней: {booking_days}")
    print(f"Итоговая стоимость: {total_price_int} руб.")
    print("Статус: ✅ Бронирование подтверждено!")
    print("=" * 45)