import argparse

from lexico import Analisador_Lexico
from sintatico import Analisador_Sintatico

def analisa_lexico(args):   
  tabela_tokens(lexical_analyzer(args))


def analisa_sintatico(args):
  analisador_sintatico = _sintatico(args)
  analisador_sintatico.log_operacoes()

#Método responsavel por retornar a lista de tokens.
def list_tokens(arquivo):
  analisador_lexico = Analisador_Lexico(arquivo)
  analisador_lexico.obter_tabela_tokens()       
  return analisador_lexico._tabela_de_simbolos

#Método do analisador léxico
def lexical_analyzer(args):
  lista_tokens = list_tokens(args)  
  return lista_tokens

#Método do analisador sintático
def _sintatico(args):
  lista_tokens = list_tokens(args)
  analisador_sintatico = Analisador_Sintatico(lista_tokens)
  analisador_sintatico.verificacao_sintatica()
  return analisador_sintatico

#Impressao da tabela de tokens
def tabela_tokens(list_tokens):
  print('*'*50)
  print('\t\t\t ANALISADOR LÉXICO \t\t\t')
  print('*'*50)
  print('[Token, Lexema, Linha, Coluna]')
  for k in (list_tokens):
    print(k)
  print('*'*50)

def all(args):
  analisa_lexico(args)
  analisa_sintatico(args)

if __name__ == '__main__':

  #cria um objeto parser
  parser = argparse.ArgumentParser(description = '*Compilador para Kinguagem')  
  parser.add_argument('-tudo','--tudo', metavar='tudo', help='exibe todas as listagens do compilador')
  parser.add_argument('-lt', '--lt',metavar='listtokens', help='exibe a listagem dos tokens')
  parser.add_argument('-ls', '--ls',metavar='parser', help='exibe o LOG do analisador sintático')
 

  args = parser.parse_args()  
  if args.tudo:
    all(args.tudo)    
  elif args.lt:
    analisa_lexico(args.lt)  
  elif args.ls:
    analisa_sintatico(args.ls)

