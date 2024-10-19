import numpy as np # Importando a biblioteca de computação numérica

# Definição de vetores
v = []
v.append(np.array([1, 1j, 1], dtype='complex128'))
v.append(np.array([4, 3, 2], dtype='complex128'))
v.append(np.array([2+3j, complex(np.sqrt(3), np.pi), 3], dtype='complex128'))
v.append(np.array([complex(np.cos(np.pi/2), np.sin(np.pi/2)), 1, complex(np.exp(-2), 0)], dtype='complex128'))

beta = []
beta.append(3+4j)
beta.append(np.exp(-np.pi/2) + 0j)
beta.append(-12345+28413j)

# Funções

def soma(u, v):
  # é só isso?? to achando que n é mas ok

  w = u + v
  return w


def produto(beta, u):
 # precisa de um módulo (no beta) e dps da multiplicação
  beta_mod = np.abs(beta)

 # agora é a multiplicação
  w = beta_mod * u

  return w


def verifica_soma(u, v):
  

  w = soma(u,v) # se for só issso eu vou surtar
                # era só isso e eu surtei
  # se w ainda for de V retorna true
  return isinstance(w, np.ndarray) #verifica se é um array(vetor)

def verifica_produto(beta, u):
  #mesma lógica do verificar soma

  w = produto(beta,u) #é só isso, eu sei


  return isinstance(w, np.ndarray)#verifica se w ainda é de V (se ss, retorna true)

print('Testando fechamento da soma:')
for i in range(len(v)):
  for k in range(len(v) - i - 1):
    print(verifica_soma(v[i], v[k+i+1]) , ' => ', v[i], ' , ', v[k+i+1])

print('--------------------------------------')
print('Testando fechamento do produto escalar:')
for i in range(len(beta)):
  for k in range(len(v)):
    print(verifica_produto(beta[i], v[k]), ' => ', beta[i], ' , ', v[k])

# proponha o vetor nulo
nulo = np.zeros(3, dtype='complex128') # nem a pau que foi tão fácil assim

def verifica_nulo(v):
  # Já implementado, não se preocupar
  return np.all(soma(v, nulo) == v) # retorna True se todos valores de v+nulo forem iguais a v e False caso contrário

print('--------------------------------------')
print('Testando vetor nulo:')
for i in range(len(v)):
  print(verifica_nulo(v[i]), ' => ', v[i])

# proponha o vetor inverso
def inverso(v):
  w = np.ones(3, dtype='complex128') # alterar?

  return w

def verifica_inverso(v):
  # Já implementado, não se preocupar
  return np.all(soma(v, inverso(v)) == nulo) # retorna True se todos valores de v+inverso(v) forem iguais a nulo e False caso contrário

print('--------------------------------------')
print('Testando vetor inverso:')
for i in range(len(v)):
  print(verifica_inverso(v[i]), ' => ', v[i])

def verifica_comutatividade(u, v):
  """
  Verifica se u + v = v + u

  @param u: Um vetor de V
         v: Um vetor de V
  @return: bool: True se os vetores forem comutativos,
                 False caso contrário.
  """
  return False

print('--------------------------------------')
print('Testando comutatividade:')
for i in range(len(v)):
  for k in range(len(v) - i - 1):
    print(verifica_comutatividade(v[i], v[k+i+1]) , ' => ', v[i], ' , ', v[k+i+1])

def verifica_associatividade(u, v, w):
  """
  Verifica se u + (v + w) = (v + u) + w

  @param v: Um vetor de V
         u: Um vetor de V
         w: Um vetor de V
  @return: bool: True se os vetores seguirem a regra da associação,
                 False caso contrário.
  """
  return False


print('--------------------------------------')
print('Testando associatividade:')
for i in range(len(v)):
  for k in range(len(v) - i - 1):
    for l in range(len(v) - i - k - 2):
      print(verifica_associatividade(v[i], v[k+i+1], v[k+i+l+2]) , ' => ', v[i], ' , ', v[k+i+1], ' , ', v[k+i+l+2])

def verifica_distributividade_1(beta, u, v):
  """
  Verifica se beta * (u + v) = beta * u + beta * v

  @param beta: Um valor escalar complexo
         u: Um vetor de V
         v: Um vetor de V
  @return: bool: True se os vetores seguirem a regra da distributividade,
                 False caso contrário.
  """
  return False

print('--------------------------------------')
print('Testando distributividade 1:')
for i in range(len(beta)):
  for k in range(len(v)):
    for l in range(len(v) - k - 1):
      print(verifica_distributividade_1(beta[i], v[k], v[k+l+1]), ' => ', beta[i], ' , ', v[k], ' , ', v[k+l+1])

def verifica_distributividade_2(beta, gamma, u):
  """
  Verifica se (beta + gamma) * u = beta * u + gamma * u

  @param beta: Um valor escalar complexo
         gamma: Um valor escalar complexo
         u: Um vetor de V
  @return: bool: True se os vetores seguirem a regra da distributividade,
                 False caso contrário.
  """
  return False

print('--------------------------------------')
print('Testando distributividade 2:')
for i in range(len(beta)):
  for k in range(len(beta) - i - 1):
    for l in range(len(v)):
      print(verifica_distributividade_2(beta[i], beta[i+k+1], v[l]), ' => ', beta[i], ' , ', beta[i+k+1], ' , ', v[l])


def verifica_distributividade_3(beta, gamma, u):
  """
  Verifica se beta * (gamma * u) = (beta * gamma) * u

  @param beta: Um valor escalar complexo
         gamma: Um valor escalar complexo
         u: Um vetor de V
  @return: bool: True se os vetores seguirem a regra da distributividade,
                 False caso contrário.
  """
  return False

print('--------------------------------------')
print('Testando distributividade 3:')
for i in range(len(beta)):
  for k in range(len(beta) - i - 1):
    for l in range(len(v)):
      print(verifica_distributividade_3(beta[i], beta[i+k+1], v[l]), ' => ', beta[i], ' , ', beta[i+k+1], ' , ', v[l])

def verifica_escalar_unitario(u):
  """
  Verifica se 1 * u = u

  @param : Um vetor de V
  @return: bool: True se os vetores seguirem a regra da distributividade,
                 False caso contrário.
  """
  return False

print('--------------------------------------')
print('Testando o axioma do escalar unitário:')
for i in range(len(v)):
      print(verifica_escalar_unitario(v[i]), ' => ', v[i])

