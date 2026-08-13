t = ('a', 'b', 'c', 'd')
print(t)

t1 = 'A',
print(t1)

t2 = t1 + t
print(t2)

t = tuple("fiap")
print(t)
print(t[1:])

# ATRIBUIÇÃO DE TUPLAS
a = 5
b = 10
print(f"a: {a}, b: {b}")

a, b = b, a
print(f"a: {a}, b: {b}")

email = "fulano@gmail.com"
username, dominio = email.split("@")
print(username)
print(dominio)