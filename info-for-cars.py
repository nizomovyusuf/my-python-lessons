# -*- coding: utf-8 -*-
"""
03/03/2024

"Info for cars" dasturi

Muallif: Yusuf Nizomov
"""

def avto_info(kompaniya, model, rangi, korobka, yili, narhi = None):
    """Avtomobil haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    avto = {'kompaniya': kompaniya,
            'model': model,
            'rangi': rangi,
            'korobka': korobka,
            'yili': yili,
            'narhi': narhi}
    return avto

def avto_kirit():
    """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida,
    ma'lumotlarni bitta ro'yxatga joylash imkonini beruvchi funksiya"""
    avtolar = []
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting:")
        kompaniya = input("Ishlab chiqaruvchi: ")
        model = input("Modeli: ")
        rangi = input("Rangi: ")
        korobka = input('Korobka: ')
        yili = input("Yili: ")
        narhi = input("Narhi: ")
        #Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida 
        #lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
        avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
        # Yana avto qo'shish-qo'shmaslikni so'raymiz
        javob = input("Yana avto qo'shasizmi? (yes/no): ")
        if javob == 'no':
            break
    return avtolar


def info_print(avto_info):
    """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi dastur"""
    print(f"Kampaniya: {avto_info['kompaniya'].upper()}, Madel: {avto_info['model'].title()}, "
          f"Rangi: {avto_info['rangi'].title()}, Karobka: {avto_info['korobka'].title()}, "
          f"Yili: {avto_info['yili']}-yil, Narhi: {avto_info['narhi']}$")
     
for avto in avto_kirit():
    info_print(avto)
    
    
    
    