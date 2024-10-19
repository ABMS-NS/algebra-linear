import numpy as np
from matplotlib import pyplot as plt

# Aquisição dos dados
i = np.array([0,0.5,1,1.5,2,2.5,3,3.5,4,4.5])
L_1 = 0.0125  # 12.5mm
L_2 = 0.025   # 25mm
L_3 = 0.05    # 50mm
L_4 = 0.1     # 100mm

f_l1 = np.array([31.5, 31.55, 31.63, 31.7, 31.74, 31.82, 31.9, 31.94, 32, 32.04])
f_l2 = np.array([30.65, 30.8, 30.92, 31.03, 31.15, 31.25, 31.36, 31.5, 31.63, 31.73])
f_l3 = np.array([37.86, 38.1, 38.31, 38.53, 38.72, 38.94, 39.15, 39.4, 39.62, 39.71])
f_l4 = np.array([40.31, 40.75, 41.15, 41.5, 41.97, 42.42, 42.83, 43.22, 43.64, 44.04])

# Plotando os dados originais
plt.figure(figsize=(10, 6))
plt.scatter(i, f_l1, c='r', label="L_1")
plt.scatter(i, f_l2, c='g', label="L_2")
plt.scatter(i, f_l3, c='b', label="L_3")
plt.scatter(i, f_l4, c='k', label="L_4")
plt.legend(loc="upper left")
plt.xlabel("Corrente")
plt.ylabel("Força magnética")
plt.title("Dados Originais")
plt.grid(True)
plt.show()

# Função para tratamento dos dados
def tratar_dados(forca, forca_inicial):
    return (forca - forca_inicial) * 9.8

# Tratamento dos dados
f_l1_novo = tratar_dados(f_l1, f_l1[0])
f_l2_novo = tratar_dados(f_l2, f_l2[0])
f_l3_novo = tratar_dados(f_l3, f_l3[0])
f_l4_novo = tratar_dados(f_l4, f_l4[0])

# Plotando os dados tratados
plt.figure(figsize=(10, 6))
plt.scatter(i, f_l1_novo, c='r', label="L_1")
plt.scatter(i, f_l2_novo, c='g', label="L_2")
plt.scatter(i, f_l3_novo, c='b', label="L_3")
plt.scatter(i, f_l4_novo, c='k', label="L_4")
plt.legend(loc="upper left")
plt.xlabel("Corrente")
plt.ylabel("Força magnética (tratada)")
plt.title("Dados Tratados")
plt.grid(True)
plt.show()

# Função para calcular B usando pseudo-inversa
def calcular_B(i, L, f):
    # Criando a matriz A = i*L
    A = i.reshape(-1, 1) * L
    # Usando a pseudo-inversa para encontrar B
    B = np.linalg.pinv(A) @ f
    return B[0]

# Calculando B para cada comprimento
B_1 = calcular_B(i, L_1, f_l1_novo)
B_2 = calcular_B(i, L_2, f_l2_novo)
B_3 = calcular_B(i, L_3, f_l3_novo)
B_4 = calcular_B(i, L_4, f_l4_novo)

print("\nValores de B encontrados:")
print(f"B1 = {B_1:.4f} mN/(A*mm)")
print(f"B2 = {B_2:.4f} mN/(A*mm)")
print(f"B3 = {B_3:.4f} mN/(A*mm)")
print(f"B4 = {B_4:.4f} mN/(A*mm)")

# Plotando os resultados finais com as curvas ajustadas
plt.figure(figsize=(10, 6))
plt.scatter(i, f_l1_novo, c='r', label="L1 observado")
plt.scatter(i, f_l2_novo, c='g', label="L2 observado")
plt.scatter(i, f_l3_novo, c='b', label="L3 observado")
plt.scatter(i, f_l4_novo, c='k', label="L4 observado")

# Adicionando as linhas de predição
plt.plot(i, i*L_1*B_1, 'r--', label="L1 predito")
plt.plot(i, i*L_2*B_2, 'g--', label="L2 predito")
plt.plot(i, i*L_3*B_3, 'b--', label="L3 predito")
plt.plot(i, i*L_4*B_4, 'k--', label="L4 predito")

plt.legend(loc="upper left")
plt.xlabel("Corrente (A)")
plt.ylabel("Força magnética (mN)")
plt.title("Força magnética vs Corrente - Dados tratados e ajustados")
plt.grid(True)
plt.show()

# Calculando e mostrando os erros médios quadráticos
def calcular_erro(i, L, B, f_obs):
    f_pred = i * L * B
    mse = np.mean((f_obs - f_pred)**2)
    return np.sqrt(mse)

print("\nErros RMS para cada ajuste:")
print(f"Erro L1: {calcular_erro(i, L_1, B_1, f_l1_novo):.4f} mN")
print(f"Erro L2: {calcular_erro(i, L_2, B_2, f_l2_novo):.4f} mN")
print(f"Erro L3: {calcular_erro(i, L_3, B_3, f_l3_novo):.4f} mN")
print(f"Erro L4: {calcular_erro(i, L_4, B_4, f_l4_novo):.4f} mN")