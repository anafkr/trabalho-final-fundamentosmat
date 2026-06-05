# Trabalho 1 - Recursividade
#  Fundamentos Matemáticos para Computação
# Exercícios: 3 (Torres de Hanói), 4 (Inversão de String), 5 (Decimal para Binário)


# --- Torres de Hanói ---

def hanoi(n, origem, destino, auxiliar):
    if n == 1:  # caso base
        print(f"Mover disco 1 de {origem} para {destino}")
        return
    hanoi(n - 1, origem, auxiliar, destino)
    print(f"Mover disco {n} de {origem} para {destino}")
    hanoi(n - 1, auxiliar, destino, origem)

print("=== Torres de Hanói ===")
n = int(input("Número de discos: "))
hanoi(n, "A", "C", "B")


# --- Inversão de String ---

def inverter_string(s):
    if len(s) <= 1:  # caso base
        return s
    return s[-1] + inverter_string(s[:-1])

print("\n=== Inversão de String ===")
s = input("Digite uma string: ")
print(f"Resultado: {inverter_string(s)}")


# --- Decimal para Binário ---

def decimal_para_binario(n):
    if n <= 1:  # caso base
        return str(n)
    return decimal_para_binario(n // 2) + str(n % 2)

print("\n=== Decimal para Binário ===")
num = int(input("Digite um número decimal: "))
print(f"Resultado: {decimal_para_binario(num)}")