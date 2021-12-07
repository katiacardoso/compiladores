import argparse
import sys 

from lexico2 import Analisador_Lexico
from sintatico2 import Analisador_Sintatico
from semantico import Analisador_Semantico
from intermediario import Intermediario
from finaaal import Codigo_Final

def analisa_lexico(args):   
  tabela_tokens(lexical_analyzer(args))


def analisa_sintatico(args):
  analisador_sintatico = _sintatico(args)
  analisador_sintatico.log_operacoes()

#log Analisador Semantico
def log_semantic_analyzer(args):
  analisador_semantico = semantic_analyzer(args)
  analisador_semantico.log_operacoes()

def log_generated_code(args):
  print("*"*60)
  print("\t \t LOG CODIGO INTERMEDIARIO") 
  print("*"*60)
  cod_intermediario = cod_intermediary(args)
  cod_intermediario.log_intermediary() 
  #cod_final = code_finally(args) 
  #print("*"*60)
  #print("\t \t  LOG GERAÇÃO DE CODIGO FINAL") 
  #print("*"*60)
  #cod_final.log_finalCode()


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

#Metodo do analisador semântico
def semantic_analyzer(args):
  lista_tokens = lexical_analyzer(args)
  _sintatico(args)  
  analisador_semantico = Analisador_Semantico(lista_tokens)  
  analisador_semantico.inicia_analise()
  return analisador_semantico

def cod_intermediary(args):
  lista_tokens = lexical_analyzer(args)
  _sintatico(args) 
  analisador_semantico = Analisador_Semantico(lista_tokens)  
  list_id =  analisador_semantico.inicia_analise()
  cod_intermediario = Intermediario(lista_tokens, list_id)  
  cod_intermediario.inicia_geracao()  
  return cod_intermediario

def code_finally(args):
  cod_intermediary(args)
  cod_final = Codigo_Final( "C:\\Users\\ktcar\\Documents\\Compiladores\\lexico\\AnaliseLexica\\arquivo_intermediario.txt")
  cod_final.inicia_geracao()
  return cod_final 


#Impressao da tabela de tokens
def tabela_tokens(list_tokens):
  print('*'*50)
  print('\t ANALISADOR LÉXICO \t')
  print('*'*50)
  print('[Token, Lexema, Linha, Coluna]')
  for k in (list_tokens):
    print(k)
  print('*'*50)

def all(args):
  analisa_lexico(args)
  analisa_sintatico(args)
  log_semantic_analyzer(args)
  log_generated_code(args)

if __name__ == '__main__':

  

  #cria um objeto parser
  parser = argparse.ArgumentParser(description = '*Compilador para Kinguagem')  
  parser.add_argument('-tudo','--tudo', metavar='tudo', help='exibe todas as listagens do compilador')
  parser.add_argument('-lt', '--lt',metavar='lista_tokens', help='exibe a listagem dos tokens')
  parser.add_argument('-ls', '--ls',metavar='analise_sintatico', help='exibe o LOG do analisador sintático')
  parser.add_argument('-lse', '--lse',metavar="analise_semantica", help="exibe o LOG do analisador semântico")
  parser.add_argument('-lgc','--lgc', metavar="cod-intermediary", help="exibe o LOG do codigo intermediário")
  parser.add_argument('-code', metavar='cod-final', help='execução do codigo final')


  args = parser.parse_args()  
  if args.tudo:
    all(args.tudo)    
  elif args.lt:
    analisa_lexico(args.lt)  
  elif args.ls:
    analisa_sintatico(args.ls)
  elif args.lse:
    log_semantic_analyzer(args.lse)
  elif args.lgc:
    log_generated_code(args.lgc)
  elif args.code:
    code_finally(args.code)