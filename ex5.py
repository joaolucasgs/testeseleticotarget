# Definindo a string a ser invertida
string = "Exemplo de string para ser invertida"

# Criando uma lista vazia para armazenar os caracteres invertidos
inverted = []

# Percorrendo a string de trás para frente e adicionando cada caracter à lista
for i in range(len(string)-1, -1, -1):
    inverted.append(string[i])

# Juntando a lista de caracteres invertidos em uma nova string
new_string = ''.join(inverted)

# Imprimindo a string invertida
print(new_string)
