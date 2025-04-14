#Marllon Silva Araujo Coelho - 627021
#Matheus Henrique de Lima - 626732

import math

def newton_raphson():
    #Definindo a função
    def f(x):
        return math.exp(-x ** 2) - x

    #Definindo a derivada
    def df(x):
        return -2 * x * math.exp(-x ** 2) - 1

    #Iniciando x0, a tolerancia e uma quantidade máxima de repetições
    x0 = 0.5  #Ponto inicial entre 0 e 1
    tolerancia = 1e-8  #Tolerância de 8 dígitos significativos
    max_iteracoes = 10  # Número máximo de iterações

    print("Equação: e^(-x^2) = x")
    print("Encontre uma aproximação para esta raiz pelo método de Newton Raphson e obtenha uma aproximação para raiz com 8 dígitos significativos. No intervalo 0 <= x <= 1.")
    print(f"Ponto inicial: x0 = {x0}\n")

    #Fazer as interações
    for i in range(max_iteracoes):
        fx = f(x0) #Calculo da função
        dfx = df(x0) #Calculo da derivada

        if abs(dfx) < 1e-12:  #Tratativa para caso tente fazer divisão por zero
            print("Derivada muito próxima de zero.")
            return None

        x1 = x0 - fx / dfx

        #Mostrando o passo a passo
        print(f"Iteração {i + 1}:")
        print(f"x{i} = {x0:.8f}")
        print(f"f(x{i}) = {fx:.8f}")
        print(f"f'(x{i}) = {dfx:.8f}")
        print(f"x{i + 1} = x{i} - f(x{i})/f'(x{i}) = {x1:.8f}\n")

        # Verifica a aproximação
        if abs(x1 - x0) < tolerancia:
            print(f"Encontrada após {i + 1} iterações!")
            print(f"Raiz encontrada: {x1:.8f}")
            return x1

        x0 = x1

    print(f"Após {max_iteracoes} interações, não foi possível encontrar a raiz")
    return None


#Executa o metodo de Newton Raphson
newton_raphson()