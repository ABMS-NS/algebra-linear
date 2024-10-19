import numpy as np

def gauss(A, B):
    """
    Resolve um sistema de equações lineares Ax = B utilizando o método de eliminação gaussiana.
    
    @param A: Uma matriz(numpy arrays) representando os coeficientes do sistema.
    @param B: Um vetor(numpy arrays) representando os termos independentes.
    
    @return: Um vetor 1D com a solução do sistema se o sistema for consistente,
             ou lança uma exceção se o sistema for singular ou indefinido.
    """
    n = len(A)
    A = np.array(A, dtype=np.float64)
    B = np.array(B, dtype=np.float64)
    A = np.hstack([A, B.reshape(-1, 1)])

    for i in range(n):
        p = np.argmax(np.abs(A[i:, i])) + i
        if A[p, i] == 0:
            raise Exception("Sistema singular ou indefinido.")

        if p != i:
            A[[i, p]] = A[[p, i]] 

        for j in range(i + 1, n):
            factor = A[j, i] / A[i, i]
            A[j, i:] -= factor * A[i, i:]

    # Substituição reversa
    X = np.zeros(n)
    for i in range(n - 1, -1, -1):
        X[i] = (A[i, -1] - np.sum(A[i, i + 1:n] * X[i + 1:])) / A[i, i]

    return X

def combinacao(vetores, vetor_alvo):
    """
    Verifica se o vetor alvo pode ser escrito como uma combinação linear dos vetores.

    @param vetores: Conjunto de vetores.
    @param vetor_alvo: Vetor que precisa ser representado como combinação linear.

    @return: bool resultado se é combinação linear ou não (True ou False)
             coef array com os coeficientes da combinação linear
    """
    n = len(vetor_alvo)  # Tamanho do vetor

    try:
        # Resolver o sistema linear
        coef = gauss(np.copy(vetores), np.copy(vetor_alvo))
        
        # Verificar se a solução é válida
        erro = np.linalg.norm(vetores @ coef - vetor_alvo)
        if erro < 1e-10:
            return True, coef
        return False, []
    except Exception as e:
        return False, []

# Testes
print('Caso 1')
vetores = np.array([[0, 0, 1], [0, 1, 0], [1, 0, 0]])
vetor_alvo = np.array([1, 2, 3])

resultado, coef = combinacao(vetores, vetor_alvo)

if resultado:
    print(coef)
else:
    print("Não é combinação linear")

print('Caso 2')
vetores = np.array([[3.5, 2.1, 2, 4], [5.25, 3.15, 3.0, 6.0], [4.2, 2.52, 2.4, 4.8], [-4.9, -2.94, -2.8, -5.6]])
vetor_alvo = np.array([1, 2, 3, 4])

resultado, coef = combinacao(vetores, vetor_alvo)

if resultado:
    print(coef)
else:
    print("Não é combinação linear")

print('Caso 3')
vetores = np.array([[np.exp(3), np.exp(-2), np.exp(-4), np.sin(np.pi/2), np.cos(np.pi/6), 0], [5.43, 13, 2.5, 1, 1, 2], [8.145, 19.5, 3.75, 1.5, 1.5, 3.], [1, 4, 7.8, np.tan(np.pi/6), np.tanh(1), 3], [1, 4, 7.8, np.tan(np.pi/6), np.tanh(1), 3]])
vetor_alvo = np.array([1, 2, 3, 4, 5, 6])

resultado, coef = combinacao(vetores, vetor_alvo)

if resultado:
    print(coef)
else:
    print("Não é combinação linear")
