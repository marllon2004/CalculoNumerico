import numpy as np

def eliminacao_gauss(A, b, debug=False):
    n = len(b)

    # Cria matriz aumentada [A|b]
    Ab = np.hstack([A.astype(float), b.reshape(n, 1).astype(float)])

    if debug:
        print("\nMatriz aumentada inicial:")
        print(Ab)

    # Fase de eliminação
    for col in range(n):
        if debug:
            print(f"\n=== Etapa {col} ===")

        # Pivoteamento parcial
        max_row = np.argmax(np.abs(Ab[col:, col])) + col
        if max_row != col:
            Ab[[col, max_row]] = Ab[[max_row, col]]
            if debug:
                print(f"Pivoteamento: trocando linha {col} com linha {max_row}")
                print(Ab)

        # Verifica se o pivô é zero (sistema singular)
        if np.isclose(Ab[col, col], 0):
            print("\nAviso: Sistema singular (determinante zero)")
            # Verifica se é impossível
            if not np.isclose(Ab[col, -1], 0):
                print("Sistema impossível - não há solução")
            else:
                print("Sistema indeterminado - infinitas soluções")
            return None

        # Eliminação
        for row in range(col + 1, n):
            fator = Ab[row, col] / Ab[col, col]
            Ab[row, col:] -= fator * Ab[col, col:]
            if debug:
                print(f"Eliminando linha {row} usando linha {col}")
                print(Ab)

    if debug:
        print("\nMatriz após eliminação:")
        print(Ab)

    # Substituição retroativa
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        x[i] = (Ab[i, -1] - np.dot(Ab[i, i + 1:n], x[i + 1:])) / Ab[i, i]

    return x


# Sistema
A = np.array([
    [3, 2, 4],
    [1, 1, 2],
    [4, 3, -2]
])
b = np.array([1, 2, 3])

# Verifica se o sistema tem solução única
det_A = np.linalg.det(A)
print(f"Determinante da matriz: {det_A:.2f}")

if np.isclose(det_A, 0):
    print("\nO sistema é singular (determinante zero). Pode ser:")
    print("1. Inconsistente (sem solução)")
    print("2. Indeterminado (infinitas soluções)")

    # Verifica inconsistência
    Ab = np.hstack([A, b.reshape(3, 1)])
    posto_A = np.linalg.matrix_rank(A)
    posto_Ab = np.linalg.matrix_rank(Ab)

    if posto_A < posto_Ab:
        print("\nSistema INCONSISTENTE - não há solução")
    else:
        print("\nSistema INDETERMINADO - infinitas soluções")
else:
    print("\nSistema com solução única")
    solucao = eliminacao_gauss(A, b, debug=True)

    if solucao is not None:
        print("\nSolução do sistema:")
        print(f"x1 = {solucao[0]:.6f}")
        print(f"x2 = {solucao[1]:.6f}")
        print(f"x3 = {solucao[2]:.6f}")

        # Verificação
        print("\nVerificação:")
        for i in range(3):
            calc = np.dot(A[i], solucao)
            print(f"Equação {i + 1}: {calc:.2f} (deveria ser {b[i]})")