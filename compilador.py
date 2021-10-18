import argparse

from codigo_lexico import Analisador_Lexico
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = "*Compilador")
    parser.add_argument('-lt', '--lt',metavar="listtokens", help="exibe a listagem dos tokens")
args = parser.parse_args() 
def log_lexical_analyzer(args):
    print_table_tokens(lexical_analyzer(args))

def list_tokens(arquivo):
  analisador_lexico = Analisador_Lexico(arquivo)
  analisador_lexico.obter_tabela_tokens()       
  return analisador_lexico._tabela_de_simbolos

def lexical_analyzer(args):
  lista_tokens = list_tokens(args)  
  return lista_tokens

def print_table_tokens(list_tokens):
    print("*"*50)
    print("\t\t\t ANALISADOR LÉXICO \t\t\t")
    print("*"*50)
    print("[Token, Lexema, Linha, Coluna]")
    for v in (list_tokens):
        print(v)
    print("*"*50)

def all(args):
     log_lexical_analyzer(args)



 
#if args.lt:
  #  log_lexical_analyzer(args.lt)
