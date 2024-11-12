import json

number = int(input("Введите номер квалификации: "))
find = False

with open("dump.json", 'r', encoding='utf-8') as file: 
    data = json.load(file) 
    for skill in data:
        if skill.get("model") == "data.skill":
            if skill["fields"].get("specialty") == number: 
                skill_code = skill["fields"].get("code")
                skill_title = skill["fields"].get("title")
                find = True
            
                for profession in data:
                    if profession.get("model") == "data.specialty":
                        specialty_code = profession["fields"].get("code")
                        if specialty_code in skill_code:  
                            specialty_title = profession["fields"].get("title")
                            specialty_educational = profession["fields"].get("c_type")
                            
                  

if not find:
    print("=============== Не Найдено ===============") 
    
else:
    print("=============== Найдено ===============") 
    print(f"{specialty_code} >> Специальность '{specialty_title}' , {specialty_educational}")
    print(f"{skill_code} >> Квалификация '{skill_title}'")