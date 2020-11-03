"""
Função que retorna true quando o número passado por parâmetro é par e retorna false caso contrário.
"""
def even(num):
  return (num % 2) == 0

"""
*********************************************Paridade Par**********************************************
Função que recebe uma palavra em binário, independente do seu tamanho, e retorna a palavra acrescida do bit de paridade par.
Caso a palavra conhenha uma quantidade par de uns, um '0' será adicionado ao início da palavra, caso contrário, um '1' será adicionado.
"""
def pair(bin):
  acum = 0
  for bit in bin:
    if (bit == '1'):
      acum += 1
  if (even(acum)):
    return '0' + bin
  else:
    return '1' + bin

"""
********************************************Paridade Ímpar*********************************************
Função que recebe uma palavra em binário, independente do seu tamanho, e retorna a palavra acrescida do bit de paridade ímpar.
Caso a palavra conhenha uma quantidade ímpar de uns, um '0' será adicionado ao início da palavra, caso contrário, '1' será adicionado.
"""
def odd(bin):
  acum = 0
  for bit in bin:
    if (bit == '1'):
      acum += 1
  if (not even(acum)):
    return '0' + bin
  else:
    return '1' + bin

"""
*****************************************Detecção de erro (Par)*****************************************
Função que checa se a palavra em binário recebida possui ou não erros de acordo com o bit de paridade par. A função retorna true quando está tudo ok com a palavra recebida, e false caso haja erro.
"""
def error_detector_even(bin):
  acum = 0
  for bit in bin:
    if bit == '1':
      acum += 1
  return even(acum)

"""
****************************************Detecção de erro (Ímpar)****************************************
Função que checa se a palavra em binário recebida possui ou não erros de acordo com o bit de paridade ímpar. A função retorna true quando está tudo ok com a palavra recebida, e false caso haja erro.
"""
def error_detector_odd(bin):
  acum = 0
  for bit in bin:
    if bit == '1':
      acum += 1
  return not even(acum)