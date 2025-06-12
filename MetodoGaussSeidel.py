import numpy as np

# Definindo o sistema
A = np.array([[10, 1, 1],
              [1, 10, 1],
              [1, 1, 10]], dtype=float)
b = np.array([12, 12, 12], dtype=float)


# Verificação do critério de Sassenfeld
def verifica_sassenfeld(A):
    n = A.shape[0]
    beta = np.zeros(n)
    print("\nCálculo dos coeficientes de Sassenfeld:")

    # β₁
    beta[0] = (abs(A[0, 1]) + abs(A[0, 2])) / abs(A[0, 0])
    print(f"β₁ = (|{A[0, 1]}| + |{A[0, 2]}|)/|{A[0, 0]}| = {beta[0]}")

    # β₂
    beta[1] = (abs(A[1, 0]) * beta[0] + abs(A[1, 2])) / abs(A[1, 1])
    print(f"β₂ = (|{A[1, 0]}|×{beta[0]} + |{A[1, 2]}|)/|{A[1, 1]}| = {beta[1]}")

    # β₃
    beta[2] = (abs(A[2, 0]) * beta[0] + abs(A[2, 1]) * beta[1]) / abs(A[2, 2])
    print(f"β₃ = (|{A[2, 0]}|×{beta[0]} + |{A[2, 1]}|×{beta[1]})/|{A[2, 2]}| = {beta[2]}")

    max_beta = max(beta)
    print(f"\nβ máximo = {max_beta}")
    if max_beta < 1:
        print("O método de Gauss-Seidel irá convergir (β < 1)")
    else:
        print("O método pode não convergir (β ≥ 1)")
    return max_beta


beta_max = verifica_sassenfeld(A)


# Implementação detalhada do Gauss-Seidel
def gauss_seidel_detalhado(A, b, tol=1e-3, max_iter=100):
    n = len(b)
    x = np.zeros(n)
    print("\nIniciando método de Gauss-Seidel:")
    print(f"Valor inicial: x = {x}\n")

    for k in range(max_iter):
        x_ant = x.copy()
        print(f"--- ITERAÇÃO {k + 1} ---")

        # Atualização de x₁
        soma = A[0, 1] * x[1] + A[0, 2] * x[2]
        x[0] = (b[0] - soma) / A[0, 0]
        print(f"x₁ = ({b[0]} - ({A[0, 1]}×{x_ant[1]} + {A[0, 2]}×{x_ant[2]})) / {A[0, 0]} = {x[0]}")

        # Atualização de x₂
        soma = A[1, 0] * x[0] + A[1, 2] * x[2]
        x[1] = (b[1] - soma) / A[1, 1]
        print(f"x₂ = ({b[1]} - ({A[1, 0]}×{x[0]} + {A[1, 2]}×{x_ant[2]})) / {A[1, 1]} = {x[1]}")

        # Atualização de x₃
        soma = A[2, 0] * x[0] + A[2, 1] * x[1]
        x[2] = (b[2] - soma) / A[2, 2]
        if(k == 0):
            x[2] = round(x[2], 3)
        print(f"x₃ = ({b[2]} - ({A[2, 0]}×{x[0]} + {A[2, 1]}×{x[1]})) / {A[2, 2]} = {x[2]}")

        erro = np.max(np.abs(x - x_ant))
        print(f"\nValor atual: x = {x}")
        print(f"Erro máximo: {erro}\n")

        if erro < tol:
            print(f"Convergência alcançada após {k + 1} iterações!")
            break

    return x


# Executando o método
solucao = gauss_seidel_detalhado(A, b)

print("\nSolução final:")
print(f"x = {solucao}")
