'''
    Desenvolva um sistema que receba o cadastro do nome de usuario e as 
    suas informações basicas, como, email e telefone, em seguida, calcule
    o gasto de combustivel mensal, considerando que o carro que ele usa tem
    capacidade total de 55 litros. Na gasolina ele tem autonomia de 14km/l, já
    no alcool a autonomia é de 12km/l. Considere que de casa ao trabalho são 32km
    e ele precisa ir e voltar do trabalho de segunda a sexta. 
        - Qual será o gasto mensal (reais/litro) que o usuario terá no alcool e na gasolina? 
        - Qual á média de kilometros rodados mensalmente?
'''

nome = input("Cadastre seu nome: ")
email = input("Cadastre seu email: ")
tel = input("Cadastre seu telefone: ")
capacidade_tanque = 55
distancia = 64
distancia_mensal = distancia/30
autonomia_gasolina = capacidade_tanque/14
autonomia_alcool = capacidade_tanque/12

print(f"Nome: {nome}")
print(f"Email: {email}@gmail.com")
print(f"Telefone: +55 61 9{tel}")

preco_gasolina = float(input("Coloque o preço da gasolina: "))
preco_alcool = float(input("Coloque o preço do álcool: "))
gasto_gasolina = capacidade_tanque*preco_gasolina
gasto_alcool = capacidade_tanque*preco_alcool
