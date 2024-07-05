"""CALCULADORA DE AÑOS MESES Y DIAS QUE TIENES"""

año_nacimiento=int(input("ingrese su año de nacimiento:"))
mes_nacimiento=int(input("ingrese su mes de nacimiento:"))
dia_nacimiento=int(input("ingrese su dia de nacimiento:"))
dia_hoy=int(input("ingrese el dia de hoy:"))
mes_hoy=int(input("ingrese el mes de hoy:"))

resultado_año = año_nacimiento - 2024
resultado_mes = mes_nacimiento-mes_hoy
resultado_dia=dia_nacimiento-dia_hoy
print(f"ustede tiene :{resultado_año} años")
print(f"tiene: {resultado_mes} meses")
print(f"tiene: {resultado_dia} dias")
