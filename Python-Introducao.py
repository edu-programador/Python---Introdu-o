## Ex 1 : Escreva na tela "Ola,Mundo"
# print("Olá,mundo")
# print('Ola,mundo!')

## Ex2: Ler uma entrada do teclado e imprimir na tela
variavel = input("Digite seu nome:")
# print(variavel)
# print("Meu nome é " + variavel)
# print(f"Meu nome é {variavel}")

## Ex 3: Leia dois numeros do teclado e exiba a soma
num1 = int(input("Diga o primeiro Numero: "))
num2 = float(input("Digite o segundo numero: "))
soma = num1 + num2
print(f"{num1} + {num2} = {soma}")


# booleano = True or True
# and -> Lembrar da multiplicação de 0 e 1
# or -> Lembrar da Soma de 0 e 1
# print(booleano)

##Ex 4: Diga se um número lido como entrada do teclado é negativo
# print("programa que testa se um número é negativo")
# num = float(input("Digite um número"))

# print((num < 0))

# if(num < 0):
#     print(f"O número {num} é negativo!")

##Ex 5: Diga se um número lido como entrada do teclado é positivo ou igual a zero
# print("programa que testa se um número é positivo ou igual a zero")
# num = float(input("Digite um número"))

# if(num >= 0):
    # print(f"O número {num} é positivo ou Zero!!")

# if( not num < 0):
#     print(f"O número {num} é positivo ou Zero!!")

## Ex6 :  Una os dois exercicios anteriores
# num = float(input("Digite um número"))

# if(num >= 0):
#     print(f"O número {num} é positivo ou Zero!!")
# else:
#     print(f"O número {num} é negativo!")

##Ex 7 : Diga se um número é positivo, negativo ou zero
# num = float(input("Digite um número"))

# if(num > 0):
#     print(f"{num} é Positivo!")
# elif(num < 0 ):
#     print(f"{num} é negativo!")
# else:
#     print(f"ZERO")

## Ex 8 : Diga duas notas de um aluno, calcule a média e diga se ele
#for aprovado ou esta de recuperação(<7)

# nota1 = float(input("Digite a primeira nota:"))
# nota2 = float(input("Digite a segunda nota:"))

# media = (nota1 + nota2)/2

# if(media >= 7):
#     print(f"Aprovado com media {media}")
# else:
#     print(f"Recuperação com media {media}")

## Ex 8 : Diga duas notas de um aluno, calcule a média e diga
# se ele
#for aprovado(media>=7) ou esta de recuperação(4<=media<7)
# ou reprovado(media<4)

# nota1 = float(input("Digite a primeira nota:"))
# nota2 = float(input("Digite a segunda nota:"))

# media = (nota1 + nota2)/2

# if(media >= 7):
#     print(f"Aprovado com media {media}")
# elif(media>=4):
#     print(f"Recuperação com media {media}")
# else:
#     print(f"Reprovado com media {media}")


## Ex 10: Leia uma idade do teclado e se for maior que 100
#ou menor que 0, diga que é invalido e pergunte novamente

# idade = int(input("Digite sua idade: "))

# while(idade <= 0 or idade >= 100):
#     print(f"Idade {idade} invalida, digite novamente!")
#     idade = int(input("Digite sua idade: "))

# print(f"Sua idade é {idade}")

## Ex11: Escreva na tela o nome Infinity School 100 vezes
# contador = 0

# while(contador < 100):
#     contador = contador + 1
#     print("Infinity School")

## Ex12: Diga quantas vezes o computador deve escrever
#Infinity School na tela
# contador = 0
# vezes = int(input("Digite o número de vezes para repetir na tela"))

# while(contador < vezes):
#     print("Infinity School")
#     contador = contador + 1

## Ex13: Escreva na tela o nome Infinity School 100 vezes com for

# for contador in range(100):
#     print("Infinity School")

# teste = list(range(5,45))
# compras = ["arroz","feijao","carne","legumes","cerveja"]
# print("Lista de compras:")
# for item in compras:
#     print(f"Item: {item}")

## Ex14: Defina um usuario e senha e peça pro usuario digitar
#permita o login apenas se for igual

# user = "luquinhas123"
# password = "luket123"

# print("Sistema de LOGIN:")
# usuario = input("Digite seu usuario:")
# senha = input("Digite sua senha:")

# while(usuario != user or password != senha):
#     print("Senha ou usuario invalido")
#     usuario = input("Digite seu usuario:")
#     senha = input("Digite sua senha:")

# while(not(usuario == user and password == senha)):
#     print("Senha ou usuario invalido")
#     usuario = input("Digite seu usuario:")
#     senha = input("Digite sua senha:")

## Ex 15: crie uma lista de compras com 5 itens e os adicone a uma lista
# lista_de_compras = []
# for i in range(5):
#     item = input("Digite o item:")
#     lista_de_compras.append(item)

# print(lista_de_compras)