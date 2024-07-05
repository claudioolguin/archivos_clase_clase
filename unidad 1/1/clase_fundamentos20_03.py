#tema de la clase diagrama de flujos
"""un astronauta necesita un programa que le indique si puede o no bajar a los planetas que visita el astronauta ingresa
la gravedad, velocidad del viento, oxigeno del aire y temperatura para verificar segun la siguentes reglas

temperatura mayor que 40 = no
temperatura menor que 5 y oxigeno menos de 10 = no
gravedad menor que 6 y viento mayor que 20 = no

si nada de esto ocurre, el astronauta puede bajar el programa debe mostrar si puede o no bajar

hay 2 condiciones mas para que el astronauta no pueda bajar:
        
        gravedad mayor que 20 =negativo 
        viento mayor que 10 y oxigeno menor que 5 = negativo
        
        sin embargo, si el astronauta tiene un traje de caminata espacial, puede ignorar los riquisitos de oxigeno y viento"""

gravedad=float(input("escriba la gravedad registrada:"))
velocidad_viento=float(input("escriba la velocidad del viento registrada:"))
oxigeno_aire=float(input("escriba el oxigeno registrado en la zona:"))
temperatura=float(input("escriba la temperatura registrada:"))

bajar="afirmativo"

if(temperatura <40):
    bajar ="negativo"
if((temperatura <5)and(oxigeno_aire>10)):
    bajar ="negativo"
    if((gravedad <6)and(velocidad_viento <20)):
        bajar="negativo"
print(bajar)
         
         
    
        