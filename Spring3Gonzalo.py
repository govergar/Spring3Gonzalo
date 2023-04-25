#importar modulos
from random import randint

#Crear lista de clientes
clientes=['Gonzalo', 'Claudia', 'Erik', 'Raul', 'Miguel', 'Francisca','Kathy', 'Nicolas', 'Andrea', 'Vidal']   

# funcion que crea contraseña
def crear_password():
    password=""
    longitud1=randint(1,2)
    longitud2=randint(1,2)
    longitud3=randint(1,2)
    for i in range(longitud1):
        i=chr(randint(65,90))
        for j in range(longitud2):
            j=chr(randint(65,90)).lower()
            for z in range(longitud3):
                z=str(randint(0,9))
            password=str((password)+i+j+z)
    return  password
#Función que pregunta y almacena número de teléfono


opc=input('Desea crear cuenta a los clientes (Si/No): ')
# creamos las cuentas de cada usuario con su respectiva contraseña
if opc=="Si":
    cuentas_password={}
    for nombre in clientes:
        cuentas_password[nombre]=crear_password()
        
else:
    print('Que tenga buen día')

print(cuentas_password)

cuentas_telefono={}
i=0
while i<len(clientes):
    aux=input('Porfavor ingrese el número de contacto de '+ clientes[i]+':')
    if len(aux)>=8:
        print('Número ingresado de forma correcta por favor ingrese el siguiente')
        cuentas_telefono[clientes[i]]=aux
        i=i+1
    else:
        print("El número de contacto debe tener al menos 8 dígitos, intente nuevamente")
        i=i
print(cuentas_telefono)  