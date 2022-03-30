# Python darslari:
# 15-dars vazifalari.
# Nesting. Lug'at ichida ro'yxat, ro'yxat ichida lug'at?

# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi 
# ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang,
# va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.

# car_0 = {
#     'model':'chevrolet',
#     't_yil':2016,
#     'probeg':15000,
#     'narx':10000,
#     'marka':'nexia'
#     }
# car_1 = {
#     'model':'lada',
#     't_yil':2008,
#     'probeg':150000,
#     'narx':5000,
#     'marka':'kalina'
#     }
# car_2 = {
#     'model':'audi',
#     't_yil':2019,
#     'probeg':9000,
#     'narx':12000,
#     'marka':'a5'
#     }   
# car = car_0
# print(f"{car['model'].title()} {car['marka']}, {car['t_yil']}-yilda ishlab chiqarilgan,\
# {car['narx']} USD")
     
# car = car_1
# print(f"{car['model'].title()} {car['marka']}, {car['t_yil']}-yilda ishlab chiqarilgan,\
# {car['narx']} USD")
      
# car = car_2
# print(f"{car['model'].title()} {car['marka']}, {car['t_yil']}-yilda ishlab chiqarilgan,\
# {car['narx']} USD")

# cars = [car_0, car_1, car_2]
# # for car in cars:
# #     print(f"{car['model']} {car['marka']}, {car['t_yil']}-yilda ishlab chiqarilgan, {car['narx']} USD")


# # print(cars[0]['model'])
# # print(cars[2]['narx'])
# print(f"{cars[0]['model'].title()} "
#       f"{cars[0]['narx']}")

# malibus = []
# for n in range(10):
#     new_car = {
#         'model':'malibu',
#         'rang':'none',
#         'yil':2022,
#         'narh':'none',
#         'km':0,
#         'korobka':'avto'
#         }
#     malibus.append(new_car)
# for malibu in malibus[:3]:
#     malibu['rang'] = 'qizil'
# for malibu in malibus[3:6]:
#     malibu['rang'] = ['qora']
# for malibu in malibus[6:]:
#     malibu['rang'] = ['oq']
#     malibu['korobka'] = 'mexanika'
    
# for malibu in malibus:
#     if malibu['korobka'] == 'avto':
#         malibu['narh'] = 40000
#     else:
#         malibu['narh'] = 36000
        
        
# for malibu in malibus:
#     print(malibu)

# dasturchilar = {
#     'ali':['c++', 'python'],
#     'vali':['sql','html'],
#     'salim':['web dizayn','ux dizayn'],
#     'farida':['css','java']
#     }
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi: ", end = '')
#     for til in tillar:
#         print(f'{til.upper()}, ', end='')


# # for ism, tillar in dasturchilar.items():
# #     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
# #     for til in tillar:
# #         print(til.upper())
        

# hamkasblar = {
#     'al':{'familiya':'kamolov',
#            'ism':'jaloliddin',
#            't_yil':1993,
#            't_shahar':'shahrixon',
#            'ish':'muhandis',
#            'tillar':['c++','php']},
#     'val':{'familiya':'jalilov',
#             'ism':'vali',
#             't_yil':1989,
#             't_shahar':'andijon',
#             'ish':'iqtisodchi',
#             'tillar':['python','java']},
#     'jama':{'familiya':'jumaboev',
#             'ism':'jamoldin',
#             't_yil':1986,
#             't_shahar':'buxoro',
#             'ish':'yurist',
#             'tillar':['css','nodejs']}
#     }
# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()}, "
#           f"{info['t_yil']}-yilda, {info['t_shahar']} shahrida tug'ilgan.\n"
#           "Quyidagi dasturlash tillarini biladi: ")
#     for til in info['tillar']:
#         print(til.upper())
        
        
# 1. Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi 
# ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, 
# va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.
# f_person0 = {
#     'ism':'buxoriy',
#     'kasb':'hadisshunos',
#     't_yil':'buxoro',
#     'va_joy':'samarqand',
#     'asar':['hamsa', 'kollej']
#     }
# f_person1 = {
#     'ism':'xorazmiy',
#     'kasb':'matematik',
#     't_yil':'xorazm',
#     'va_joy':'urganch',
#     'asar':['tib qonunlari', 'maktab']
#     }
# f_person2 = {
#     'ism':'ibn sino',
#     'kasb':'tabib',
#     't_yil':'navoi',
#     'va_joy':'toshkent',
#     'asar':['algebra', 'kulol']
#     }
# f_person3 = {
#     'ism':'alisher navoiy',
#     'kasb':'shoir',
#     't_yil':'hirot',
#     'va_joy':'shahrisabz',
#     'asar':['al jome as sahih', 'tabib']
#     }
# persons = [f_person0, f_person1, f_person2, f_person3]
# for ism in persons:
#     print(f"{ism['ism'].title()} {ism['t_yil'].title()} shahrida tug'ilgan.\
# Kasbi {ism['kasb']} va {ism['va_joy'].title()} shahrida vafot etgan")

# 2.Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham 
# qo'shing. For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.

# f_person0 = {
#     'ism':'buxoriy',
#     'kasb':'hadisshunos',
#     't_yil':'buxoro',
#     'va_joy':'samarqand',
#     'asar':['hamsa', 'kollej']
#     }
# f_person1 = {
#     'ism':'xorazmiy',
#     'kasb':'matematik',
#     't_yil':'xorazm',
#     'va_joy':'urganch',
#     'asar':['tib qonunlari', 'maktab']
#     }
# f_person2 = {
#     'ism':'ibn sino',
#     'kasb':'tabib',
#     't_yil':'navoi',
#     'va_joy':'toshkent',
#     'asar':['algebra', 'kulol']
#     }
# f_person3 = {
#     'ism':'alisher navoiy',
#     'kasb':'shoir',
#     't_yil':'hirot',
#     'va_joy':'shahrisabz',
#     'asar':['al jome as sahih', 'tabib']
#     }
# persons = [f_person0, f_person1, f_person2, f_person3]

# for per in persons:
#     ism = per['ism']
#     asar = per['asar']
#     print(f"\n{ism.title()}ning mashxur asarlari quyidagilar: ")
#     for asa in asar:
#         print(asa.title())
    
# 3. Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang.
# Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida 
# lug'artga saqlang. Natijani konsolga chiqaring.

# kinolar = {
#     'ali':['titanic','avatar', 'avangers'],
#     'vali':['hobbit','home alone','spider man'],
#     'jack':['king artur','matrix','batman'],
#     }
# for name, film in kinolar.items():
#     print(f"\n{name.title()}ning sevimli kinolari quyidagilar:")
#     for fil in film:
#         print(fil.title())

# 4. Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni 
# lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga chiqaring.

# davlatlar = {
#     'uzbekistan':{
#         'poytaxt':'toshkent',
#         'axolisi':36000000,
#         'vil_soni':12,
#         'puli':'sum'
#         },
#     'england':{
#         'poytaxt':'london',
#         'axolisi':86000000,
#         'vil_soni':18,
#         'puli':'funt sterling'
#         },
#     'turkey':{
#         'poytaxt':'stambul',
#         'axolisi':82000000,
#         'vil_soni':21,
#         'puli':'lira'
#         }
#     }
# for dav, info in davlatlar.items():
#     poytaxt = info['poytaxt']
#     axoli = info['axolisi']
#     vil_soni = info['vil_soni']
#     puli = info['puli']
#     print(f"\n{dav.title()}ning poytaxti {poytaxt.title()}\n"
#           f"axolisi {axoli} kishi, \n"
#           f"{vil_soni} ta viloyatdan iborat, \n"
#           f"hamda pul birligi {puli}")

# 5. Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, 
# foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat sizning lug'atingizda 
# mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.

# davlatlar = {
#     'uzbekistan':{
#         'poytaxt':'toshkent',
#         'axolisi':36000000,
#         'vil_soni':12,
#         'puli':'sum'
#         },
#     'england':{
#         'poytaxt':'london',
#         'axolisi':86000000,
#         'vil_soni':18,
#         'puli':'funt sterling'
#         },
#     'turkey':{
#         'poytaxt':'stambul',
#         'axolisi':82000000,
#         'vil_soni':21,
#         'puli':'lira'
#         }
#     }
# surov = input('Davlat nomini kiriting: ').lower()
# if surov in davlatlar:
#     info = davlatlar[surov]
#     print(f"{surov.title()}ning poytaxti {info['poytaxt'].title()} shahri,"
#           f"axoli soni {info['axolisi']} kishi,\n"
#           f"viloyatlar soni {info['vil_soni']} "
#           f"hamda pul birligi {info['puli']}")
# else:
#     print("Bizda bunday davlat haqida ma'lumot mavjud emas")
    
          
    
        
        
        
    



