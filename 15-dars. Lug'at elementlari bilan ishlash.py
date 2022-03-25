# Python darslari:
# 15-dars vazifalari.
# Lug'at elementlari bilan ishlash.



# 1. Python izohli lug'atini yarating va lug'atga kamida 10 ta 
# so'z qo'shing. Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, 
# alifbo ketma-ketligida chiroyli qilib konsolga chiqaring. 

# pytho = {
#     'int':'butun son',
#     'float':"o'nlik son",
#     'string':'matn',
#     'if':'agar',
#     'else':'aks holda',
#     'elif':'aks holda, agar',
#     'strip':'ikki chekkadan tozalash',
#     'keys':'kalit suz, lugatdagi chap tomon',
#     'values':'qiymat, lugatdagi ung tomon',
#     'set':'ikki marta takrorlashni oldini oladi',
#     'tulip':'uzgarmas qiymat'
#     }
# for k,v in sorted(pytho.items()):
#     print(f"{k.title()} - {v.title()}")

# 2. Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, 
# keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.
# countries = {
#     'england':'london',
#     'spain':'madrid',
#     'germany':'berlin',
#     'russia':'moscow',
#     'usa':'vashington',
#     'uzbekistan':'tashkent',
#     'china':'beijing',
#     'kore':'seoul',
#     'japan':'tokyo'
#     }
# print("Dunyo davlatlari")
# for country in sorted(countries.keys()):
#     if country == 'usa':
#         print(f"{country.upper()}")
#     else:
#         print(f"{country.title()}")
    

# print("Davlatlarning poytaxtlari:")
# for capital in sorted(countries.values()):
#     print(f"{capital}")

# 3. Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning 
# poytaxtini konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, 
# "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.

# user = input("Qaysi davlatning poytaxtini bilishni xohlaysiz? ")
# tel = countries.get(user)
# if tel == None:
#     print("Ushbu davlat ro'yxatda mavjud emas")
# else:
#     print(f"{user.title()}ning poytaxti {tel.title()} shahri")

# 4. Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting).
# Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan 
# taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, 
# aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
# menu = {
#     'osh':20000,
#     'lagmon':15000,
#     'shashlik':12000,
#     'bishteks':20000,
#     'mastava':13000,
#     'somsa':6000,
#     'manti':11000,
#     'lavash':22000,
#     'hamburger':17000,
#     'stake':50000
#     }
# user = []
# for n in range(3):
#     user.append(input(f"Iltimos {n+1}-taom nomini kiriting: "))
    
# for buy in user:
#     if buy in menu:
#         print(f"{buy.title()}ning narxi {menu[buy]}")
#     else:
#         print(f"Kechirasiz bizda {buy} yo'q")
    
    


    
 