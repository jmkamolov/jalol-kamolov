# Python darslari:
# 14-dars vazifalari.


# 1. otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga 
# shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, 
# shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga 
# chiqaring :Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan

# otam = {'ismi':'murodjon', 't_yil':1961, 'shahri':'shahrixon'}
# t_yil = otam['t_yil']
# ism = otam['ismi']
# shahar = otam['shahri']
# print(f"Otamning ismi {ism.title()}, {t_yil}-yilda, {shahar.title()} shahrida tug'ilgan")

# 2. Oila a'zolaringizning sevimli taomlari lug'atini tuzing.
#  Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. Kamida 
#  uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh

# taomlar = {'dadam':'moshkuchuri',
#            'onam':'qovurdoq',
#            'singlim':'stake',
#            'akam':'osh',
#            'ukam':'qovurma lagmon'
#            }
# taom = taomlar['ukam']
# print(f"Akrom akamning sevimli taomi {taom}")

# 3. Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z 
# (atamani) kiriting (masalan integer, float, string, if, else va hokazo) va 
# har birining qisqacha tarjimasini yozing.

# lugat = {'integer':'butun son',
#           'float':"o'nlik son",
#           'string':'matn',
#           'if':'agar',
#           'else':'aks holda',
#           'elif':'aks holda, agar',
#           'tulip':"o'zgarmas qiymat",
#           'strip':"chap va o'ng tomondan tozalash",
#           'lstrip':'chap tomondan tozalash',
#           'rstrip':"o'ng tomondan tozalash"
#           }

# 4. Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan 
# chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.

# suz = input("Iltimos, kalit so'z kiriting: ")
# print(lugat.get(suz, 'Bunday ism mavjud emas'))

# 5. Yuqoridagi vazifani if-else yordamida qiling va natijani ham 
# foydalanuvchiga tushunarli ko'rinishda chiqaring.

# kalit = input("Iltimos kalit so'z kiriting: ")
# son = lugat.get(kalit)
# if kalit == None:
#     print("Bizda bunday so'z mavjud emas.")
# else:
#     print(f"{kalit.title()} so'zi {son} deb tarjima qilinadi")


    





