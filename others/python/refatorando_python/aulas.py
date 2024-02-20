from src.modulos import tools
from src.classe.carro import Carro
import math
import os

# ---------------------- Hello World -------------------------------------------
print("Hello, World!")

# ---------------------- Variaveis e tipos de Dados ----------------------------
nome = "Paulinho"
idade = 22
gosto_de = "software development"

print(f"My name's {nome}.")
print(f"I like {gosto_de}.")
print(f"I'm {idade} years old.")
print(f"{nome} like {gosto_de} and he's {idade} years old.")

'''
    Tipos de variaveis:
    - String: "frases"  "12564"  "casa10"
    - Int: 22  55  34655  -15
    - Float: 0.5  7.84
    - Boolean: true / false
'''

# ---------------------- Trabalhando com Números -------------------------------
num1 = 5
num2 = 3.5

print(type(num1))
print(type(num2))

a = float(num1)
print(a)
print(type(a))

b = int(num2)
print(b)
print(type(b))

x = "5"
y = "3.5"

print(type(x))
print(type(y))

x = int(x)
y = int(float(y)) # em string com casa decimal não converte direto para integer

print(x)
print(type(x))
print(y)
print(type(y))


num1 = 10
num2 = 2

print(num1 + num2) # soma
print(num1 - num2) # subtração
print(num1 * num2) # multiplicação
print(num1 / num2) # divisão
print(num1 % num2) # resto da divisão
print(num1 ** num2) # exponenciação
print(num1 // num2) # divisão inteira

'''
    Ordem de Precedencia:
    1 - ( )
    2 - **
    3 - * and / 
    4 - + and -
'''

print(3 + 5 * 7 + 3)
print((3 + 5) * (7 + 3))

print(abs(-12)) # módulo
print(pow(3,3)) # exponenciação
print(max(1,5,17,85)) # retorna o valor maximo
print(min(1,5,17,85)) # retorna o valor minimo
print(round(8.8)) # arredondamento por aproximação
print(math.floor(8.8)) # arredondamento para baixo
print(math.ceil(8.8)) # arredondamento para cima
print(math.sqrt(9)) # raiz quadrada

# ---------------------- Trabalhando com Strings -------------------------------
minha_string = "qualquer texto"

print(type(minha_string))
print(f"contatenar {minha_string} em string")

print(minha_string.upper()) # transforma em maiusculas
print(minha_string.lower()) # transforma em minusculas
print(minha_string.capitalize()) # tranforma as primeiras letras em maiusculas
print(minha_string.isupper()) # verifica se a string esta em maiuscula e retorna Trur or False
print(minha_string.strip()) # remove espaços do inicio e do final da string
print(minha_string.replace("u", "U", 1)) # troca a palavra escolhida por outra
print(len(minha_string)) # tamanho da string
print(minha_string[2]) # retorna a letra de acordo com o indice
print(minha_string[2:5]) # retorna a letra de acordo com o indice
print(minha_string[-4:-1]) # retorna a letra de acordo com o indice
print(minha_string.index("tex")) # retorna indice de acordo com o texto passado

x = "texto" in minha_string
print(x)

minha_string = "linha 1, \nlinha 2, \nlinha 3." # \n faz uma quebra de linha
print(minha_string)

minha_string = "adiciona entre \"aspas\" no texto" # \ serve como uma tecla de escape
print(minha_string)

# ---------------------- Input, Comentários e Calculadora Básica ---------------
name = input("Digite seu nome: ")
print(f"Hello, {name}")
age = int(input(f"What's your age, {name}? "))
nascimento = 2024 - age

print("=-=-=-=-=-=-==-=-=-=-=-=")
print(f"Name: {name} \nAge: {age} \nNascimento: {nascimento}")

num1 = float(input("Digite um numero: "))
num2 = float(input("Digite outro numero: "))

soma = num1 + num2
print(f"Soma: {soma}")

# ---------------------- Collections, Lists e Tuples ---------------------------
familia = ["Paulinho", "Ana", "Gabriel", "Nida", "Val"]
#              0         1        2         3      4
#             -5        -4       -3        -2     -1 
print(familia[1]) # retorna um indice
print(familia[-3]) # retorna um indice de traz pra frente
print(familia[0:3]) # retorna do indice 0 até o 3 excluindo o 3
print(familia[3:]) # retorna apartir do indice 3

print(familia)
familia[1] = "Ana Clara" # substitui o elemento do indice
print(familia)

familia.extend(["Pretinho", "Maria"]) # adiciona uma nova lista ou elemento
print(familia)

familia.append("Renato") # adiciona um elemento
print(familia)

familia.insert(5, "Josefa") # inseri o elemento no indice escolhido 
print(familia)

familia.pop() # remove o ultimo elemento
print(familia)

familia.remove("Josefa") # remove o elemento escolhido
print(familia)

print(familia.index("Val")) # retorna o indice do elemento

print(familia.count("Gabriel")) # retorna elementos iguais a na lista

# familia.clear() # limpa a lista
print(familia)

idade_familia = [22, 12, 4, 55, 55]
print(idade_familia)

idade_familia.reverse() # inverte a ordem da lista
print(idade_familia)

idade_familia.sort() # ordenar a lista em ordem crescente ou alfabética
print(idade_familia)
idade_familia.sort(reverse=True) # ordenar a lista em ordem decrescente
print(idade_familia)

familia2 = familia # copia por referencia se alterar uma tb altera a outra (mesmo espaço de memória)
print(familia2)
familia2.remove("Maria")
print(familia)
print(familia2)

familia3 = familia.copy() # cria uma nova variavel com uma cópia da outra lista (outro espço de memória)
print(familia3)
familia3.remove("Pretinho")
print(familia3)
print(familia)

coordenadas = (-49, -36) # tuplas são imultaveis
print(coordenadas)

# ---------------------- Funções em Python -------------------------------------
def big_mac():
    print("sanduiche BigMac")

print("inicio")
big_mac()
print("fim")

print()

def fazer_big_mac(name):
    print(f"sanduiche BigMac, {name}")

def fazer_batata(tamanho):
    print(f"batata {tamanho}")

def preparar_refrigerante(tipo, tamanho):
    print(f"{tipo} {tamanho}")

fazer_big_mac("Paulinho")
fazer_batata("grande")
preparar_refrigerante("Guarana", "Medio")

print()

def montar_combo(nome, tamanho_batata, tipo_refri, tamanho_refri):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    preparar_refrigerante(tipo_refri, tamanho_refri)

montar_combo("Ana Clara", "pequena", "coca", "média")

print()

def soma_num(num1, num2):
    return num1 + num2

resultado_func = soma_num(15, 20)
print(resultado)

print()

def maior_num(lista_num):
    lista_num.sort(reverse=True)
    maior_valor = lista_num[0]
    return maior_valor

resultado_func = maior_num([321, 654, 798, 2, 165, -1, 52, -46, -3654, 2, 7])
print(resultado)

# -------- If... Else statement, Operadores Lógicos e Comparações --------------
tenho_sede = True

if tenho_sede:
    print("beber agua")

print("vida que segue")

print()

esta_frio = False

if esta_frio:
    print("colocar casaco")
else:
    print("vestir camiseta")
    
print()
    
tenho_sede = False
tenho_fome = True

if tenho_sede or tenho_fome:
    print("vou na cozinha")
else:
    print("ficar vendo netflix")
    
print()

estou_em_dieta = False

if tenho_sede and tenho_fome:
    print("fazer sanduiche e coca")
elif tenho_sede and not tenho_fome:
    if estou_em_dieta:
        print("tomar agua")
    else:
        print("beber uma coquinha")
elif not(tenho_sede) and tenho_fome:
    print("fazer um sanduiche")
else:
    print("não tenho nem fome nem sede")

print()

num1 = 5
num2 = 32

if num1 == num2:
    print("numeros iguais")
elif num1 != num2:
    print("valores diferentes")
    
print()
    
if num1 > num2:
    print("num1 é maior que o num2")
elif num1 >= num2:
    print("num1 é maior ou igual que o num2")
elif num1 < num2:
    print("num1 é menor que o num2")
elif num1 <= num2:
    print("num1 é menor ou igual que o num2")
  
'''
    operadores lógicos:
    or    -> ou
    and   -> e
    not() -> negação
'''

'''
    operadores de comparação:
    == -> igual
    != -> diferente
    >  -> maior
    <  -> menor
    >= -> maior ou igual
    <= -> menor ou igual
'''

# ---------------------- loops: while e for ------------------------------------
i = 1

while (i < 10):
    print(i)
    i += 1
    
print(i)
    
while True: # looping infinito no caso de não houver um breake dentro do while
    break

print()

lista = ["Paulinho", "Gabriel", "Ana"]

for item in lista:
    print(item)
    
print()

canal = "refatorando"

for letra in canal:
    print(letra)

print()

for index in range(0,20,2):
    print(index)
    
print()

for index in range(len(lista)):
    print(f"{lista[index]:8} --> {index:>2}")
    
print()

for index in range(5):
    if index == 0:
        print("primeira linha")
    else:
        print(f"{index+1}° linha")

print()

matriz_numeros = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0],
] 

for linha in matriz_numeros:
    # print(linha)
    print("----------")
    for coluna in linha:
        print(coluna)

# ---------------------- coleções: sets e dictinary ----------------------------
# sets são listas desordenadas na qual se pode adicionar e remover elementos mas não alteralos
set1 = {"maça","laranja","abacaxi"}
set1.add("pera")
set1.remove("maça")
# set1.pop() #remove o ultimo valor
print(set1)

print()

set2 = {0,3,57,-74}
set3 = {True,False,False,False}
set4 = {"Paulinho",22,True,1.80,60}
print(set4)

print()

# dicionario são multaveis e possui chave e valor
meses = {
    "Jan" : "Janeiro",
    "Fev" : "Fevereiro",
    "Mar" : "Março",
    "Abr" : "Abril",
    "Mai" : "Maio",
    "Jun" : "Junho",
    "Jul" : "Julho",
    "Ago" : "Agosto",
    "Set" : "Setembro",
    "Out" : "Outubro",
    "Nov" : "Novembro",
    "Dze" : "Dezembro",
}

print(meses)
print(meses["Jul"]) # chamando com colchetes valores errados vai dar erro
print(meses.get("Mai")) # chamando com get valores errados retornara None
print(meses.get("Ago","Padrão")) 
print(meses.get("ABC","Padrão")) # retorna um valor padrão caso o primeiro seja invalido

print(len(meses))
print(len(set3))

# ---------------- Tratando exceção - try...except...finally -------------------
try:
    numero = int(input("Digite um numero: "))
    print(numero)
except ZeroDivisionError:
    print("Divisão por zero não é possivel.")
except ValueError:
    print("Digite um valor valido.")
except:
    print("Erro inesperado.")
finally:
    print("Sempre Executa.")

# ---------------------- manipulando arquivos ----------------------------------
# open("caminho", "modo")
'''
    modos:
    r  -> leitura
    a  -> append / incrementar
    w  -> write / escrita - quando adiciona algum ele primeiro limpa o arquivo
    x  -> criar arquivo
    r+ -> leitura + escrita
'''

arquivo1 = open("src/test.txt", "r")
print(arquivo1.readable())
print(arquivo1.read())
print(arquivo1.readline())

lista = arquivo1.readlines()
print(lista)
# print(lista[4])
arquivo1.close()

# arquivo2 = open("src/test2.txt", "a")
# arquivo2.write("\nSQL")
# print(arquivo2)
# arquivo2.close()

# arquivo3 = open("src/test3.txt", "x")
# arquivo3.write("Python\n")
# print(arquivo3)
# arquivo3.close()

print()

if os.path.exists("src/test2.txt"):
    os.remove("src/test2.txt")
else:
    print("Arquivo inexistente")
    
print()

if os.path.exists("tempCodeRunnerFile.py"):
    os.remove("tempCodeRunnerFile.py")
else:
    print("Arquivo inexistente")

print()

if os.path.exists("nova_pasta"):
    os.rmdir("nova_pasta")
else:
    print("Diretório inexistente")

# ---------------------- modulos e pip -----------------------------------------
print(tools.PI)
print(tools.GRAVITY)
print(tools.get_extension("test.txt"))
print(tools.highest_number([1,55,-28,33]))

'''
    PIP
    - gerenciador de pacotes
    - pip --version -> mostra a versão
    - pip install   -> para instalar pacotes
    - pip install <pacote> -t .\libs   -> para instalar pacotes e uma pasta do pacote
    - pip uninstall   -> para remover pacotes
    - https://docs.python.org/3/py-modindex.html -> lista de modulos ja disponiveis para usar
    - pip install -r requirements.txt -t .\libs -> instalando todas as libs de uma vez através do arquivo requirements.txt
'''

# ---------------------- orientação a objetos ----------------------------------
i13 = Carro("BMW", "i13", "Preto", "Eletrico")

i13.ligar()
i13.ligar()
i13.acelerar()
i13.acelerar()
i13.acelerar()
i13.acelerar()
i13.acelerar()
i13.acelerar()
i13.desacelerar()
i13.desacelerar()
i13.desacelerar()
i13.desacelerar()
i13.desacelerar()
i13.desacelerar()
i13.desacelerar()
i13.desligar()

f40 = Carro("Ferrari", "F40", "Vermelho", "Gasolina")
model_s = Carro("Tesla", "Model S", "Branco", "Eletrico")
