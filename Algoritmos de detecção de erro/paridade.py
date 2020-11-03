"""
Função que retorna true quando o número passado por parâmetro é par e retorna false caso contrário.

***********************************************Exemplos************************************************
num = 1                                                                     num = 4
retorno = False                                                             retorno = True
"""
def even(num):
  return (num % 2) == 0

"""
*********************************************Paridade Par**********************************************
Função que recebe uma palavra em binaryário, independente do seu tamanho, e retorna a palavra acrescida do bit de paridade par.
Caso a palavra conhenha uma quantidade par de uns, um '0' será adicionado ao início da palavra, caso contrário, um '1' será adicionado.

***********************************************Exemplos************************************************
binary = '0100001'                                                          binary = '1100001'
retorno = '00100001'                                                        retorno = '11100001'
"""
def pair(binary):
  acum = 0
  for bit in binary:
    if (bit == '1'):
      acum += 1
  if (even(acum)):
    return '0' + binary
  else:
    return '1' + binary

"""
********************************************Paridade Ímpar*********************************************
Função que recebe uma palavra em binaryário, independente do seu tamanho, e retorna a palavra acrescida do bit de paridade ímpar.
Caso a palavra conhenha uma quantidade ímpar de uns, um '0' será adicionado ao início da palavra, caso contrário, '1' será adicionado.

***********************************************Exemplos************************************************
binary = '0100001'                                                          binary = '1100001'
retorno = '10100001'                                                        retorno = '01100001'
"""
def odd(binary):
  acum = 0
  for bit in binary:
    if (bit == '1'):
      acum += 1
  if (not even(acum)):
    return '0' + binary
  else:
    return '1' + binary

"""
*****************************************Detecção de erro (Par)*****************************************
Função que checa se a palavra em binaryário recebida possui ou não erros de acordo com o bit de paridade par. A função retorna true quando está tudo ok com a palavra recebida, e false caso haja erro.

***********************************************Exemplos*************************************************
binary = '00100001'                                                          binary = '10100001'
retorno = True                                                               retorno = False
"""
def error_detector_even(binary):
  acum = 0
  for bit in binary:
    if bit == '1':
      acum += 1
  return even(acum)

"""
****************************************Detecção de erro (Ímpar)****************************************
Função que checa se a palavra em binaryaryário recebida possui ou não erros de acordo com o bit de paridade ímpar. A função retorna true quando está tudo ok com a palavra recebida, e false caso haja erro.

***********************************************Exemplos*************************************************
binary = '10100001'                                                             binary = '00100001'
retorno = True                                                               retorno = False
"""
def error_detector_odd(binary):
  acum = 0
  for bit in binary:
    if bit == '1':
      acum += 1
  return not even(acum)