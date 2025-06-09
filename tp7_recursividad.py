# TP7 - Recursividad

# 1. Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def mostrar_factoriales(hasta):
    for i in range(1, hasta + 1):
        print(f"{i}! = {factorial(i)}")

# 2. Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def mostrar_fibonacci(hasta):
    for i in range(hasta + 1):
        print(f"F({i}) = {fibonacci(i)}")

# 3. Potencia
def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

# 4. Decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

# 5. Palíndromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

# 6. Suma de dígitos
def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

# 7. Pirámide de bloques
def bloques_piramide(n):
    if n == 0:
        return 0
    return n + bloques_piramide(n - 1)

# 8. Contar dígitos
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

# Ejemplos de uso
if __name__ == "__main__":
    print("1. Factoriales hasta 5:")
    mostrar_factoriales(5)

    print("\n2. Serie de Fibonacci hasta 7:")
    mostrar_fibonacci(7)

    print("\n3. Potencia 2^5 =", potencia(2, 5))

    print("\n4. Decimal 13 a binario =", decimal_a_binario(13))

    print("\n5. ¿'reconocer' es palíndromo?", es_palindromo("reconocer"))

    print("\n6. Suma de dígitos de 1234 =", suma_digitos(1234))

    print("\n7. Bloques para pirámide de altura 4 =", bloques_piramide(4))

    print("\n8. Contar cuántas veces aparece el dígito 3 en 13353 =", contar_digito(13353, 3))
