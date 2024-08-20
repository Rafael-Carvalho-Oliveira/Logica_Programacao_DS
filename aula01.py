nome = "Karython"
#idade = 25
peso = 85.8
altura = 1.75
instrutor = True

# FIXME: Entrada de dados

sobrenome = input("Digite o seu sobrenome:")
print(nome, sobrenome)
print(type(sobrenome))

idade = input("Digite sua idade:")

print(type(idade))
idade = int(idade)
print(type(idade))

ano = int(input("em que ano você nasceu?"))
print(type(ano))
if ano > 2024:
    print("tu nem nasceu porra")
else:
    print("sei la")
    
