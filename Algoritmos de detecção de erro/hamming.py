"""
Função que converte um inteiro para string de binários com tamanho
definido.
"""
def int_to_bin(number, padding):
    return (bin(number)[2:]).zfill(padding)

"""
Função que converte uma string de binários para inteiro.
"""
def bin_to_int(binary):
    return int(binary, 2)

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
Função que corrige um binário recebendo o index do bit que está errado.
"""
def corrector(binary, index):
  result = ""
  for i in range(len(binary)):
    if i == (index-1):
      if(binary[i] == '0'): result += '1'
      else: result += '0'
    else:
      result += binary[i]
  return result

"""
Função que realiza a decodificação e a correção do código de Hamming.
"""
def decode(binary):
   # Lista contendo os binários dos índices dos uns de binary
  list_ones = get_index_element_equals_1(binary)

  # Fazendo xor nos índices dos uns
  result = list_inversor(loop_xor(list_ones))

  # Índices dos uns contidos em result
  ones_of_result = get_index_element_equals_1(result)

  if ones_of_result == []:
    print("\nSem erros! :)")
  else:
    data = list(binary)
    c,ch,error,h,parity_list,h_copy=0,0,0,[],[],[]

    for i in range(len(data)):
      p=(2**c)
      h.append(int(data[i]))
      h_copy.append(data[i])
      if(p==(i+1)):
          c=c+1

    for parity in range((len(h))):
      ph=(2**ch)
      if(ph==(parity+1)):

          startIndex=ph-1
          i=startIndex
          toXor=[]

          while(i<len(h)):
              block=h[i:i+ph]
              toXor.extend(block)
              i+=2*ph

          for z in range(1,len(toXor)):
              h[startIndex]=h[startIndex]^toXor[z]
          parity_list.append(h[parity])
          ch+=1
    parity_list.reverse()
    error=sum(int(parity_list) * (2 ** i) for i, parity_list in enumerate(parity_list[::-1]))

    # Caso não encontre erro
    if((error)==0):
      print("\nSem erro! :)")

    # Caso erro esteja fora do escopo
    elif((error)>=len(h_copy)):
      print('\nErro não pôde ser detectado :/')

    # Caso erro tenha sido enconrtado
    else:
      print('\nErro foi encontrado no bit ' + str(error) + " :c\nA mensagem correta deveria ser:")
      print(corrector(binary, error))


"""
***********************************************Exemplos*************************************************
* Codificação -> entrada: 0011  saída: 1000011
                 entrada: 0101011   saída: 11001010011

* Decodificação -> entrada: 1000011   saída: Sem erro! :)
                   entrada: 1100011   saída: Erro no bit 2
                   entrada: 11001010011   saída: Sem erro! :)
                   entrada: 10001010011   saída: Erro no bit 2
                   
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
    decode(binary)
    break
  else:
    print("Opção inválida, tente novamente!")