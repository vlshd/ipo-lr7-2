import json

# Получаем номер квалификации от пользователя
number = int(input("Введите номер квалификации: "))
find = False  # Флаг для отслеживания, была ли найдена квалификация

# Открываем файл с данными в формате JSON
with open("dump.json", 'r', encoding='utf-8') as file: 
    data = json.load(file)  # Загружаем данные из файла
    
    # Перебираем все элементы в данных
    for skill in data:
        # Ищем элементы, где модель равна "data.skill"
        if skill.get("model") == "data.skill":
            # Проверяем, совпадает ли номер квалификации
            if skill["fields"].get("specialty") == number: 
                skill_code = skill["fields"].get("code")  # Получаем код квалификации
                skill_title = skill["fields"].get("title")  # Получаем название квалификации
                find = True  # Обновляем флаг, что квалификация найдена
                
                # Перебираем все элементы еще раз для поиска соответствующей специальности
                for profession in data:
                    if profession.get("model") == "data.specialty":
                        specialty_code = profession["fields"].get("code")  # Получаем код специальности
                        if specialty_code in skill_code:  
                            specialty_title = profession["fields"].get("title")  # Получаем название специальности
                            specialty_educational = profession["fields"].get("c_type")  # Получаем тип образования

# Если квалификация не найдена, выводим соответствующее сообщение
if not find:
    print("=============== Не Найдено ===============") 
    
# Если квалификация найдена, выводим информацию о ней и соответствующей специальности
else:
    print("=============== Найдено ===============") 
    print(f"{specialty_code} >> Специальность '{specialty_title}' , {specialty_educational}")
    print(f"{skill_code} >> Квалификация '{skill_title}'")
