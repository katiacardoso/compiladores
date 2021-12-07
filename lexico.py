import sys
import os.path

class Analisador_Lexico:
    def __init__(self,arquivo_fonte):
      self._cabeca=0
      self._fita=[]
      self._numero_da_linha=1
      self._tabela_de_simbolos=[]
      self._lexema=''
      self._fim_linha='\n'
      self._especiais = ['(',')',';','=','+','-','*','/','==','<','\"']
      self._arquivo_fonte = arquivo_fonte
      if not os.path.exists(self._arquivo_fonte):
       # self._arquivo_fonte.write('Arquivo de entrada inexistente')
        print('Erro Geral: Arquivo {0} nao foi encontrado.'.format(self._arquivo_fonte))
      else:
        self._arquivo=open(self._arquivo_fonte,'r')

    def _avancar_cabeca(self):
      self._cabeca += 1
    def _posicao_cabeca(self):
      return self._cabeca
    def _atualizar__numero_linha(self):
      self._numero_da_linha += 1

    def _obter_caracter(self): #retorna o prox _caractere na fita e avança a cabeça de leitura
      if self._cabeca<len(self._fita):
        self._letra = self._fita[self._cabeca]
        self._avancar_cabeca()
        if self._letra != self._fim_linha or not self._letra.isspace():
          self._lexema += self._letra
        return self._letra
      else:
        return '\n'

    def obter_tabela_tokens(self):
      #print(self._arquivo)
      for self._linha in self._arquivo:
        self._fita = list(self._linha)
        self._q0()
        self._atualizar__numero_linha()
        self._cabeca = 0
      self._arquivo.close()
      return self._tabela_de_simbolos   #retorna a lista dos tokens reconhecidos

    def _q0(self):
      self._caracter = self._obter_caracter()
      if 'e' == self._caracter:
        self._q1()
      elif 'k' == self._caracter:
        self._q15()
      elif 's' == self._caracter:
        self._q24()
      elif 'f' == self._caracter:
        self._q31()
      elif 'l' == self._caracter:
        self._q45()
      elif '+' == self._caracter:
        self._q50()
      elif '-' == self._caracter:
        self._q51()
      elif '*' == self._caracter:
        self._q52()
      elif '/' == self._caracter:
        self._q53()
      elif '(' == self._caracter:
        self._q54()
      elif ')' == self._caracter:
        self._q55()
      elif '<' == self._caracter:
        self._q56()
      elif '=' == self._caracter:
        self._q57()
      elif ';' == self._caracter:
        self._q58()
      elif '==' == self._caracter:
        self._q59()
      elif '\"' == self._caracter:
        self._q62()
      elif self._fim_linha == self._caracter:
        pass
      elif self._caracter.isdigit():
        self._q60()
      elif self._caracter.islower():
        self._q61()
      elif self._caracter.isspace():
        self._lexema = ''
        self._q0()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q1(self):
      self._caracter = self._obter_caracter()
      if 's' == self._caracter:
        self._q2()
      elif 'n' == self._caracter:
        self._q8()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))
        

    def _q2(self):
      self._caracter = self._obter_caracter()
      if 'k' == self._caracter:
        self._q3()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))
          
    def _q3(self):
      self._caracter = self._obter_caracter()
      if 'r' == self._caracter:
        self._q4()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))
          

    def _q4(self):
      self._caracter = self._obter_caracter()
      if 'e' == self._caracter:
        self._q5()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))
        
    def _q5(self):
      self._caracter = self._obter_caracter()
      if 'v' == self._caracter:
        self._q6()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))
      
    def _q6(self):
      self._caracter = self._obter_caracter()
      if 'a' == self._caracter:
        self._q7()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q7(self):
      # reconhece o comando eskreva     
      self._caracter = self._obter_caracter()
      if self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['eskreva',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['eskreva',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._q0() 
        
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['eskreva',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))
          
    def _q8(self):
      self._caracter = self._obter_caracter()
      if 'k' == self._caracter:
        self._q9()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q9(self):
      self._caracter = self._obter_caracter()
      if 'u' == self._caracter:
        self._q10()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))
      
    def _q10(self):
      self._caracter = self._obter_caracter()
      if 'a' == self._caracter:
        self._q11()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q11(self):
      self._caracter = self._obter_caracter()
      if 'n' == self._caracter:
        self._q12()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))


    def _q12(self):
      self._caracter = self._obter_caracter()
      if 't' == self._caracter:
        self._q13()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q13(self):
      self._caracter = self._obter_caracter()
      if 'o' == self._caracter:
        self._q14()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q14(self):
      # reconhece o comando eskuanto
      self._caracter = self._obter_caracter()
      if self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['enkuanto',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['enkuanto',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._q0()
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['enkuanto',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))
      
    def _q15(self):
      self._caracter = self._obter_caracter()
      if 'i' == self._caracter:
        self._q16()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q16(self):
      self._caracter = self._obter_caracter()
      if 'n' == self._caracter:
        self._q17()
      elif 'm' == self._caracter:
        self._q22()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q17(self):
      self._caracter = self._obter_caracter()
      if 'i' == self._caracter:
        self._q18()
      elif 't' == self._caracter:
        self._q23()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q18(self):
      self._caracter = self._obter_caracter()
      if 'c' == self._caracter:
        self._q19()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q19(self):
      self._caracter = self._obter_caracter()
      if 'i' == self._caracter:
        self._q20()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q20(self):
      self._caracter = self._obter_caracter()
      if 'o' == self._caracter:
        self._q21()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q21(self):
      # reconhece o comando kinicio
      self._caracter = self._obter_caracter()
      if self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kinicio',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kinicio',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._q0()
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kinicio',self._lexema,self._numero_da_linha,self._cabeca])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))
      
    def _q22(self):
      #reconhece o comando kim
      self._caracter = self._obter_caracter()
      if self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kim',self._lexema,self._numero_da_linha,self._cabeca])
        self._lexema = ''
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kim',self._lexema,self._numero_da_linha,self._cabeca])
        self._lexema = ''
        self._q0()
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kim',self._lexema,self._numero_da_linha,self._cabeca])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))
    
    def _q23(self):
      #reconhece o comando kint 
      self._caracter = self._obter_caracter()
      if self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kint',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kint',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._q0()
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kint',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q24(self):
      self._caracter = self._obter_caracter()
      if 'e' == self._caracter:
        self._q25()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))
            
    def _q25(self):
      self._caracter = self._obter_caracter()
      if 'k' == self._caracter:
        self._q26()
      elif 'n' == self._caracter:
        self._q27()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q26(self):
      #reconhece o comando sek
      self._caracter = self._obter_caracter()
      if self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['sek',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['sek',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._q0()
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['sek',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q27(self):
      self._caracter = self._obter_caracter()
      if 'a' == self._caracter:
        self._q28()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q28(self):
      self._caracter = self._obter_caracter()
      if 'o' == self._caracter:
        self._q29()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))        

    def _q29(self):
      self._caracter = self._obter_caracter()
      if 'k' == self._caracter:
        self._q30()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q30(self):
      #reconhece o comando senaok
      self._caracter = self._obter_caracter()
      if self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['senaok',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['senaok',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._q0()
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['senaok',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q31(self):
      self._caracter = self._obter_caracter()
      if 'i' == self._caracter:
        self._q32()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q32(self):
      self._caracter = self._obter_caracter()
      if 'm' == self._caracter:
        self._q33()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q33(self):
      self._caracter = self._obter_caracter()
      if 's' == self._caracter:
        self._q34()
      elif 'e' == self._caracter:
        self._q37()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q34(self):
      self._caracter = self._obter_caracter()
      if 'e' == self._caracter:
        self._q35()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))        

    def _q35(self):
      self._caracter = self._obter_caracter()
      if 'k' == self._caracter:
        self._q36()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q36(self):
      #reconhece o comando fimsek
      self._caracter = self._obter_caracter()
      if self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['fimsek',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['fimsek',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._q0()
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['fimsek',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))              

    def _q37(self):
      self._caracter = self._obter_caracter()
      if 'n' == self._caracter:
        self._q38()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))
          
    def _q38(self):
      self._caracter = self._obter_caracter()
      if 'k' == self._caracter:
        self._q39()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q39(self):
      self._caracter = self._obter_caracter()
      if 'u' == self._caracter:
        self._q40()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q40(self):
      self._caracter = self._obter_caracter()
      if 'a' == self._caracter:
        self._q41()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q41(self):
      self._caracter = self._obter_caracter()
      if 'n' == self._caracter:
        self._q42()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q42(self):
      self._caracter = self._obter_caracter()
      if 't' == self._caracter:
        self._q43()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q43(self):
      self._caracter = self._obter_caracter()
      if 'o' == self._caracter:
        self._q44()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q44(self):
      #reconhece o comando fimenkuanto
      self._caracter = self._obter_caracter()
      if self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['fimenkuanto',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['fimenkuanto',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._q0()
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['fimenkuanto',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q45(self):
      self._caracter = self._obter_caracter()
      if 'e' == self._caracter:
        self._q46()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q46(self):
      self._caracter = self._obter_caracter()
      if 'i' == self._caracter:
        self._q47()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q47(self):
      self._caracter = self._obter_caracter()
      if 'a' == self._caracter:
        self._q48()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q48(self):
      self._caracter = self._obter_caracter()
      if 'k' == self._caracter:
        self._q49()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))        

    def _q49(self):
      #reconhece o comando leiak
      self._caracter = self._obter_caracter()
      if self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['leiak',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['leiak',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._q0()
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['leiak',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q50(self):
      #reconhece o simbolo +
      self._tabela_de_simbolos.append(['+',self._lexema,self._numero_da_linha,self._cabeca])
      self._lexema = ''
      self._q0()

    def _q51(self):
      #reconhece o simbolo -
      self._tabela_de_simbolos.append(['-',self._lexema,self._numero_da_linha,self._cabeca])
      self._lexema = ''
      self._q0()
      
    def _q52(self):
      #reconhece o simbolo *
      self._tabela_de_simbolos.append(['*',self._lexema,self._numero_da_linha,self._cabeca])
      self._lexema = ''
      self._q0()

    def _q53(self):
      #reconhece o simbolo /
      self._tabela_de_simbolos.append(['/',self._lexema,self._numero_da_linha,self._cabeca])
      self._lexema = ''
      self._q0()

    def _q54(self):
      #reconhece o simbolo (
      self._tabela_de_simbolos.append(['(',self._lexema,self._numero_da_linha,self._cabeca])
      self._lexema = ''
      self._q0()

    def _q55(self):
      #reconhece o simbolo )
      self._tabela_de_simbolos.append([')',self._lexema,self._numero_da_linha,self._cabeca])
      self._lexema = ''
      self._q0()

    def _q56(self):
      #reconhece o simbolo <
      self._tabela_de_simbolos.append(['<',self._lexema,self._numero_da_linha,self._cabeca])
      self._lexema = ''
      self._q0()

    def _q57(self):
      #reconhece o simbolo =
      self._caracter = self._obter_caracter()
      #print(self._caracter)
      if '=' == self._caracter:
        self._q59()
      elif self._caracter:
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['=',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      else:
         print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))


    def _q59(self):
      #reconhece o simbolo ==
      self._caracter = self._obter_caracter()
      while self._caracter.isdigit() or self._caracter.islower(): 
        self._caracter = self._obter_caracter()
      if self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['==',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['==',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._q0()
      elif self._caracter in self._especiais:
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['==',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))
        exit()


    def _q58(self):
      #reconhece o simbolo ;
      self._tabela_de_simbolos.append([';',self._lexema,self._numero_da_linha,self._cabeca])
      self._lexema = ''
      self._q0()

    def _q60(self):
      #reconhece  numeros
      self._caracter = self._obter_caracter()
      while self._caracter.isdigit(): 
        self._caracter = self._obter_caracter()
      if self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['numeko',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['numeko',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._q0()
      elif self._caracter in self._especiais:
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['numeko',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q61(self):
      #reconhece identificadores
      self._caracter = self._obter_caracter()
      while self._caracter.isdigit() or self._caracter.islower(): 
        self._caracter = self._obter_caracter()
      if self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._q0()
      elif self._caracter in self._especiais:
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))
        exit()

    def _q62(self):
      self._caracter = self._obter_caracter()
      '''if self._caracter.isdigit() or self._caracter.islower():
        self._q61()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()'''

      if self._caracter.isdigit() or self._caracter.isalpha() or self._caracter.isspace() or self._caracter == "!" or self._caracter == ",":
            self._q63()

      elif self._caracter == "\"":  # logo nao vai existir texto entre eles, ou seja nao precisa da etapa q42.
            self._q64()
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))

    def _q63(self):
      self._caracter = self._obter_caracter()
      '''if self._caracter == '\"':
        self._q64()
      elif self._caracter.isdigit() or self._caracter.isalpha() or self._caracter.isspace() or self._caracter == "!" or self._caracter == ",":
        self._q61()
      elif self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = '' 
      elif self._caracter in self._especiais: 
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['kid',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._cabeca -= 1
        self._q61()'''
      '''else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))'''
      
      if self._caracter.isdigit() or self._caracter.isalpha() or self._caracter.isspace() or self._caracter == "!" or self._caracter == "," or self._caracter == ":":
        self._q63()
      elif self._caracter == "\"":
        self._q64()

      else: #Situacao screen("Teste); <- erro, entretando é necessário tratar o erro.
            
        print("Erro Léxico: não foi possivel encontrar um token valído na linha {0} coluna {1}. Caracter {2} invalido ou nao esperado.".format(self._numero_da_linha, self._cabeca - len(self._lexema), self._caracter))
        self._lexema = " "
        self._cabeca -= 1            
        self._q0()
        exit()

    def _q64(self):
    #reconhece string
      self._caracter = self._obter_caracter()
      if self._fim_linha == self._caracter:
        self._tabela_de_simbolos.append(['string',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
      elif self._caracter.isspace():
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['string',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._q43()
      elif self._caracter in self._especiais:
        self._lexema = self._lexema[:len(self._lexema)-1]
        self._tabela_de_simbolos.append(['string',self._lexema,self._numero_da_linha,self._cabeca-1])
        self._lexema = ''
        self._cabeca -= 1
        self._q0()
      else:
        print('Erro léxico ({0},{1}): _caracter {2} inesperado'.format(self._numero_da_linha, self._cabeca,self._caracter))
        

'''_automato = Analisador_Lexico(sys.argv[2])
_tabela =_automato.obter_tabela_tokens()
print('\n')
print('[TOKENS,LEXEMA,LINHA,COLUNA]')
for i in range(len(_tabela)):
  print(_tabela[i]) '''
