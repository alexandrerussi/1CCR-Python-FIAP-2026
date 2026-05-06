lista_frutas = ["Banana", "Morango", "Manga"]

# lista_frutas[0] = "Banana"
# lista_frutas[1] = "Morango"
# lista_frutas[2] = "Manga"
print(lista_frutas[1])
lista_frutas.append("Goiaba")
print(lista_frutas[-1])
print()

for i in range(len(lista_frutas)):
    print(lista_frutas[i])

print()

for fruta in lista_frutas:
    print(fruta)