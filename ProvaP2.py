# Danielle Barros Bassetto - 629391
# Marllon Silva Araujo Coelho - 627021

# usada para trabalhar com vetores e cálculos numéricos
import numpy as np

# função para calcular a área sob a curva: f(x) = 1 / (1 + x)
# isso é o que será "integrado"
def f(x):
    return 1 / (1 + x)

# intervalo onde queremos calcular a área sob a curva
# de a = 0 até b = 3
a = 0
b = 3

# define quantos pedaços (ou subintervalos) o intervalo será dividido
# aqui usamos n = 6 pedaços. Quanto maior esse número, mais preciso o resultado.
n = 6

# calcula o tamanho de cada pedaço (ou largura de cada trapézio)
# h é a distância entre os pontos no eixo x
h = (b - a) / n

# cria uma lista de pontos igualmente espaçados de a até b (inclusive), com n+1 pontos
x = np.linspace(a, b, n + 1)

# calcula os valores da função f(x) para cada ponto x. Isso nos dá as alturas dos trapézios.
y = f(x)

# Regra dos Trapézios
# calcula a área total aproximada somando a área de todos esses trapézios
integral = (h / 2) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])

# passo a passo

print("Passo 1: Definir parâmetros")
print(f"a = {a}, b = {b}, n = {n}, h = {h:.2f}\n")

print("Passo 2: Pontos de avaliação")
# mostra os pontos em x onde a função será avaliada
for i, xi in enumerate(x):
    print(f"x_{i} = {xi:.1f}")
print()

print("Passo 3: Calcular a função nos pontos")
# mostra os valores da função f(x) em cada ponto x
for i, (xi, yi) in enumerate(zip(x, y)):
    print(f"f({xi:.1f}) = {yi:.6f}")
print()

print("Passo 4: Regra do trapézio")
# mostra como a fórmula da Regra dos Trapézios é aplicada com os valores calculados
print(f"Integral ≈ (h/2) * [f(x₀) + 2f(x₁) + ... + f(x₆)]")
print(
    f"≈ ({h:.2f}/2) * [{y[0]:.6f} + 2*{y[1]:.6f} + 2*{y[2]:.6f} + 2*{y[3]:.6f} + 2*{y[4]:.6f} + 2*{y[5]:.6f} + {y[6]:.6f}]")
print(
    f"≈ {h / 2:.2f} * [{y[0]:.6f} + {2 * y[1]:.6f} + {2 * y[2]:.6f} + {2 * y[3]:.6f} + {2 * y[4]:.6f} + {2 * y[5]:.6f} + {y[6]:.6f}]")
print(f"≈ {h / 2:.2f} * {y[0] + 2 * np.sum(y[1:-1]) + y[-1]:.6f}")
print(f"≈ {integral:.6f}")

# para verificar se o resultado aproximado está certo, usamos uma função da biblioteca scipy
# essa função calcula o valor exato da integral (ou seja, a área real sob a curva)
from scipy.integrate import quad

# quad retorna o valor exato da integral da função f entre a e b
exact, _ = quad(f, a, b)

# mostra o valor exato e o erro da aproximação
print(f"\nValor exato: {exact:.6f}")
print(f"Erro: {abs(integral - exact):.6f}")
