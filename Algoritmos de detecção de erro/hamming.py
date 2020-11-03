"""
Função que retorna um lista que guarda todas as posições de potências de 2 possíveis de acordo com o tamanho da cadeia de bits recebida. n é o limite superior.
O while usa a expressão (2**i)-1, pois python conta índices de 0 até n-1, e não de 1 até n.
"""
def get_index_range_power2(n):
  index_list = []
  i = 0
  while (2**i)-1 <= n:
    index_list.append((2**i)-1)
    i += 1
  return index_power2

def get_index_element_equals_1(binary):
  index_list = []
  for i in range(len(bin)):
    if bin[i] == '1':
      index_list.append(i)