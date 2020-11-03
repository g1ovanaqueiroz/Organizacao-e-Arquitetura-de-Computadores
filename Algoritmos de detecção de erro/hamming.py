"""
Função que converte um inteiro para string de binários com tamanho
definido.
"""
def int_to_bin(number, padding):
    return (bin(number)[2:]).zfill(padding)

"""
Função que retorna a quantidade de potências de dois existentes até o limite n (len de binary).
O while usa a expressão (2**i)-1, pois python conta índices de 0 até n-1, e não de 1 até n.
"""
def len_power2(binary):
  i = 0
  while (2**i)-1 <= len(binary):
    i += 1
  return i

"""
Função que retorna uma lista com todos as de potências de 2 até o limite n. Essa lista poderá ser usada como range para iteração sobre listas.
"""
def range_len_power2(n):
  index_list = []
  for i in range(n):
    index_list.append((2**i)-1)
  return index_list

"""
Função que recebe uma lista e retorna uma String com os elementos da lista em ordem.
"""
def list_to_string(list):
  result = ""
  for elem in list:
    result += elem
  return result

"""
Essa função retorna o tamanho total da mensagem correta a ser enviada.
"""
def total_len(binary):
  return len_power2(binary) + len(binary)

"""
Função que retorna uma lista com todos os índices (em binário) dos bits iguais a '1' da cadeia de bits recebida como parâmetro.
"""
def get_index_element_equals_1(binary):
  index_list = []
  for i in range(len(binary)):
    if binary[i] == '1':
      index_list.append(int_to_bin(i+1, len_power2(binary)))
  return index_list

"""
Função que retorna a lista invertida
"""
def list_inversor(binary):
  return list(binary[::-1])

"""
Função que retorna um xor feito com cada membro de uma lista de binários recebida como parâmetro.
"""
def loop_xor(bins):
  result = bins[0]
  for i in range(1, len(bins)):
    result = xor(result, bins[i])
  return result

"""
Função que retorna o resultado de um xor entre dois elementos binários.
"""
def xor(a, b):
  result = ""
  for i in range(len(a)):
    if a[i] == b[i]:
      result += '0'
    else:
      result += '1'
  return result

"""
Função que realiza a codificação do código de Hamming.
"""
def encode(binary):
  # Lista que vai conter os elementos do retorno do programa
  result = []

  # Criando lista com cada bit da cadeira de bits recebida
  copy_binary = []
  for bit in binary:
    copy_binary.append(bit)

  # Lista com os índices dos bits de controle
  control_bits_index = range_len_power2(len_power2(binary))

  # Adicionando elementos de binary na string de retorno
  for i in range(total_len(binary)):
    if i in control_bits_index:
      result.append('0')
    else:
      result.append(copy_binary.pop(0))

  # Lista contendo os binários dos índices dos uns de binary
  list_ones = get_index_element_equals_1(list_to_string(result))

  # Gerando bits de controle
  control_bits = list_inversor(loop_xor(list_ones))

  # Adiciona um bit de controle qnd está no índice de algum bit de controle, caso contrário, adiciona um bit da cadeia de bits recebida
  for i in range(total_len(binary)):
    if i in range_len_power2(len_power2(binary)):
      result[i] = control_bits.pop(0)

  return list_to_string(result)

"""
Função que realiza a decodificação do código de Hamming.
Retorna True quando não há erro, e False caso haja erro.
"""
def decode(binary):
  # Lista contendo os binários dos índices dos uns de binary
  list_ones = get_index_element_equals_1(binary)

  # Fazendo xor nos índices dos uns
  result = list_inversor(loop_xor(list_ones))

  # Índices dos uns contidos em result
  ones_of_result = get_index_element_equals_1(result)

  return ones_of_result == []


"""
***********************************************Exemplos*************************************************
* Codificação -> entrada: 0011  saída: 1000011
                 entrada: 0101011   saída: 11001010011

* Decodificação -> entrada: 1000011   saída: True
                   entrada: 1100011   saída: False
                   entrada: 11001010011   saída: True
                   entrada: 10001010011   saída: False
                   
"""


print("*************************Olá, seja bem vindo!*************************\n * Digite 1 para função de codificar do código Hamming. \n * Digite 2 para função de decodificar do código Hamming.")

while True:
  entrada = input()
  if entrada == '1':
    print("Digite o binário desejado:")
    binary = input()
    print("\nMensagem codificada:\n" + encode(binary))
    break
  if entrada == '2':
    print("\nDigite o binário desejado:")
    binary = input()
    if(decode(binary)): print("\nSem erros! :)")
    else: print("\niiih... Algo de errado não está certo...")
    break
  else:
    print("Opção inválida, tente novamente!")