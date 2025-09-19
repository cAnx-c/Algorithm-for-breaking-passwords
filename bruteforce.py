import time

alf = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ123456790_!#$%&()*+,-./:;<=>?@[]^`{|}~"

def combinaciones (longitud_prox, longitud_act):
    if len(longitud_act) == longitud_prox:
        yield longitud_act
    else:
        for i in alf:
            yield from combinaciones(longitud_prox, longitud_act + i)

def bruteforce (pswd):
    intentos = 0
    inicio = time.time()
    for letra in range(1, len(pswd) + 1):
        for intento in combinaciones(letra, ""):
            intentos += 1
            if intento == pswd:
                final = time.time()
                print(f"Contraseña encontrada: {intento}")
                print(f"Número de intentos: {intentos}")
                print(f"El tiempo de ejecución fue: {final - inicio:.4f} segundos")
                return intento

bruteforce("abc")
