# 1. сбор данных от пользователя
name = input("ваше имя: ")
age_str = input("ваш возраст: ")
subjects_str = input("любимые предметы (через запятую): ")

# 2. создание словаря
student = {"name": name, "age": age_str,"subjects": subjects_str}

# 3. красивый вывод анкеты
print("=" * 30)
print("АНКЕТА СТУДЕНТА")
print("=" * 30)

print(f"имя: {student['name']}")
print(f"возраст: {student['age']}")
print(f"любимые предметы: {student['subjects']}")

print("=" * 30)
