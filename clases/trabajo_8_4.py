class NumeroDebeSerPositivo(Exception):
    pass

def ingrese_numero():
    palabra = input("ingrese un numero:")
    numero = input("ingrese un numero:")
    if numero < 0:
        raise NumeroDebeSerPositivo()
    return numero 
def main():
    while True:
        palabra= input("ingrese un numero:")
        numero= ingrese_numero()
        try:
            palabra2= input("ingrese el numero 2:")
            numero2= ingrese_numero()
            print("la suma de los dos numeros es: ", numero + numero2)
            if numero2 < 0:
                raise Exception("El numero es menor que 0")
            print("la division de los dos numeros es: ", numero / numero2)
        except ValueError as e:
            print("Le dije que ingrese un numero, no un texto")
        except ZeroDivisionError as e:
            print("No se puede dividir por cero")