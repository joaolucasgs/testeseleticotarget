# Solicita ao usuário um número para calcular a sequência de Fibonacci
num = int(input("Informe um número para calcular a sequência de Fibonacci: "))

# Define os dois primeiros termos da sequência
a, b = 0, 1
fibonacci = [0, 1]

# Calcula a sequência de Fibonacci até o número informado pelo usuário
while b < num:
    a, b = b, a + b
    fibonacci.append(b)

# Verifica se o número informado pertence à sequência
if num in fibonacci:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
