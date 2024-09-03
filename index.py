def contar_letra_a(s):
    contagem = s.lower().count('a')
    if contagem > 0:
        print(f"A letra 'a' aparece {contagem} vezes na string.")
    else:
        print("A letra 'a' não aparece na string.")

# Exemplo de uso:
string = input("Informe uma string: ")
contar_letra_a(string)

