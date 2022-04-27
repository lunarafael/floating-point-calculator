import math
import struct

#Função usando struct para transformar float em binário
def float_binario(num):
    return ''.join('{:0>8b}'.format(c) for c in struct.pack('!f', num))

#Função usando struct para transformar double em binário
def double_binario(num):
    return ''.join('{:0>8b}'.format(c) for c in struct.pack('!d', num))

#Função usando struct para transformar float em hexadecimal
def float_hexa(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])

valor = float(input("\nValor a ser calculado: "))

#Coleta de valores em binários e hexadecimal
vbinario = float_binario(valor)
vhexa = float_hexa(valor)
vdouble = double_binario(valor)

#Definição do sinal
if valor >= 0:
    sinal = 0
else:
    sinal = 1
    valor = -valor

#Pegar expoente na base 2
expoente = int(math.log2(valor))

#Expoente somado com 127
expoentesomaf = expoente+127

#Soma do sinal + o binário do expoente + 127 para achar o expoente em 8 bits
bin_expo = str(sinal) + str(bin(expoentesomaf)[2:])

#Remoção dos caracteres do expoente em 8 bits para achar a mantissa
mantissa = str(vbinario)[len(bin_expo):]

#Notação do ponto flutuante (expoente + 127 em binário)
notacao = bin(expoente+1023)[2:]

print("\n==================================================================================================")
print(f"Notação do ponto flutuante precisão simples: {bin(expoentesomaf)[2:]}")
print(f"Notação do ponto flutuante precisão dupla: {notacao}")
print(f"Conversão de float para binário: {vbinario}")
print(f"Conversão de double para binário: {vdouble}")
print("==================================================================================================")
print(f"Sinal: {sinal}")
print(f"Expoente: 2^{expoente}, {expoentesomaf}, {expoente+1023}")
print(f"Mantissa: {mantissa}")
print("==================================================================================================")
print(f"Conversão para hexadecimal: {vhexa}")
print("==================================================================================================")