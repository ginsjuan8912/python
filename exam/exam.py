arr = [7,4,3,5,6,7,8,3,2,4,6]

numero1 = 1
numero2= 2
resultado= "el resultado de la suma es "+str(numero1+numero2)
print(resultado)

def letras_en_palabra(letra_1, letra_2, palabra):
    if letra_1 in palabra:
      print("La primera letra está en la palabra")
      if letra_2 in palabra:
        print("La segunda letra está en la palabra")
    else:
      print("Ninguna letra está en la palabra")

letras_en_palabra('d','b','abc')

def comparar(a, b):

    if b > a:
        print("b es mayor que a")
    elif a == b:
        print("a y b son iguales")
    else:
        print("a es mayor que b")

comparar(200,201)

def mi_funcion(x):
    for i in range(x):
        if x % (i+1) == 0:
            return True
    return False

print(mi_funcion(12))
print(mi_funcion(21))

def funcion(palabra):
    respuesta = ""
    contador = 0
    for letra_actual in palabra:
        contador_actual = 0
        for letra in palabra:
            if letra == letra_actual:
                contador_actual += 1
        if contador < contador_actual:
            respuesta = letra_actual
            contador = contador_actual
    return respuesta

print(funcion('vesuvius'))


def calcular_suma(a, b):
    indice = a
    suma = 0
    while indice <= b:
        suma+=indice
        indice+=1
    return suma

print(calcular_suma(1,3))

def es_palindromo(frase):
    frase = frase.replace(" ","")
    palindromo = False
    i=0
    while i < len(frase)//2 and not palindromo:
        if frase[i] != frase[-i]:
            palindromo = True
        i+=1
    return palindromo

print(es_palindromo('anita lava la tina'))

def invertir_palabra(palabra):
    respuesta = ""
    i=0
    while i < len(palabra):
        respuesta+=palabra[len(palabra)-1-i]
        i+=1
    return respuesta

print(invertir_palabra('carlos'))

mi_lista = [1,2,3]
mi_lista.append(mi_lista[-1])
mi_lista.remove(1)
mi_lista.insert(0,mi_lista[-2])
mi_lista = mi_lista[1:-1]
print(mi_lista)

def listar_listas_anidadas(lista_inicial): 
    lista_resultado = [[],[]]
    for elemento in lista_inicial:
        if type(elemento) == int: #Verifica si el tipo de dato es entero
            lista_resultado[0].append(elemento)
        else:
            lista_resultado[1].append(elemento)
    return lista_resultado

print(listar_listas_anidadas([1, 2, 3, 'a', 'b', 'a1', 'b1']))

mi_diccionario = {"Antonia":4.5, "Fernando":3.5, "Jose Luis":1.5}
del mi_diccionario["Jose Luis"]
mi_diccionario["Marco"] = mi_diccionario["Antonia"]-0.5
mi_diccionario["Antonia"]+=0.5
print(mi_diccionario)



def funcion(lista): 
    n = len(lista)-1 
    respuesta="" 
    while n>0: 
        if len(lista [n]) > len(respuesta): 
            respuesta = lista [n] 
            n-=1 
        else: 
            n-=1 
    return respuesta

print(funcion(['Pablito ', 'clavó ', 'un', 'clavito'] ))

def operar_en_lista(lista):
    n = len(lista)
    i = 0
    while i < n:
        j = 0
        while j < (n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            j += 1
        i += 1
    return lista

print(operar_en_lista([5,10,7]))