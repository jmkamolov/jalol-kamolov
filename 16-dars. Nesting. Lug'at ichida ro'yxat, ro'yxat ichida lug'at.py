# Python darslari:
# 15-dars vazifalari.
# Nesting. Lug'at ichida ro'yxat, ro'yxat ichida lug'at?

# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi 
# ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang,
# va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.

ilm1 = {
    'ism':'beruniy',
    'tug_yil':810,
    'shahar':'khorazm',
    'yosh':65
    }
ilm2 = {
        'ism':'ibn sino',
        'tug_yil':1010,
        'shahar':'arkbuloq',
        'yosh':58
        }
ilm3 = {
        'ism':'alisher navoiy',
        'tug_yil':1441,
        'shahar':'hirot',
        'yosh':60
        }
ilm4 = {
        'ism':'farobiy',
        'tug_yil':1665,
        'shahar':'quva',
        'yosh':71
        }
ilm = [ilm1, ilm2, ilm3, ilm4]
for il in ilm:
    print(f"{il['ism'].title()}, "
          f"{il['tug_yil']}-yilda, "
          f"{il['shahar'].title()} shahrida tug'ilgan")
    









