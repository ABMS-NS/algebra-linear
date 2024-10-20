import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

# Função para leitura dos arquivos WAV
def read(file):
    sample_rate, data = wav.read(file)
    if len(data.shape) == 2:  # Verifica se tem 2 canais
      data = np.mean(data, axis=1)
    return sample_rate, data

# Leitura dos arquivos de áudio, coloque nos arquivos do collab e fora do ./sample_data
rate1, audio1 = read("audio1.wav")
rate2, audio2 = read("audio2.wav")

min_len = min(audio1.shape[0], audio2.shape[0])
audio1 = audio1[:min_len]
audio2 = audio2[:min_len]

time1 = np.linspace(0., len(audio1) / rate1, len(audio1))
time2 = np.linspace(0., len(audio2) / rate2, len(audio2))

result = audio1 + audio2
# pode colocar aqui audio1 + audio2 para soma
# 2 * audio1 para multiplicação de escalar
# result = np.zeros_like(audio1)
# result = audio1 + (-audio1) para inversão de fase

result_time = np.linspace(0., len(result) / rate1, len(result))

# Plot do audio1
plt.subplot(3, 1, 1)
plt.plot(time1, audio1, label="Áudio 1")
plt.xlabel("Tempo [s]")
plt.ylabel("Amplitude")
plt.legend()

# Plot do audio 2
plt.subplot(3, 1, 2)
plt.plot(time2, audio2, label="Áudio 2")
plt.xlabel("Tempo [s]")
plt.ylabel("Amplitude")
plt.legend()

# Plot do result
plt.subplot(3, 1, 3)
plt.plot(result_time, result, label="Resultado")
plt.xlabel("Tempo [s]")
plt.ylabel("Amplitude")
plt.legend()

result = np.int16(result)
wav.write("resultado.wav", rate1, result) # O arquivo fica nos arquivos do Collab