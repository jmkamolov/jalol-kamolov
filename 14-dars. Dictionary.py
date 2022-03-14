# Python darslari:
# 14-dars vazifalari.


# 1. otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga 
# shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, 
# shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga 
# chiqaring :Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan

otam = {'ismi':'murodjon', 't_yil':1961, 'shahri':'shahrixon'}
t_yil = otam['t_yil']
ism = otam['ismi']
shahar = otam['shahri']
print(f"Otamning ismi {ism.title()}, {t_yil}-yilda, {shahar.title()} shahrida tug'ilgan")