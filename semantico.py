import sys

class Analisador_Semantico:
    def __init__ (self, lista_tokens):
        #declara as funções iniciais
        self.list_tokens = list(lista_tokens)
        self.symbol_table = {} 
        self.arquivo = open("log_operacao.txt",'w')
        #print(lista_tokens)
    def inicia_analise(self):
        list_t = []
        i = 0
        
        for list_t in self.list_tokens:
            atribuicao = ""           
                    
            if(list_t[0] == 'kint'):                    
                self.verifica_existencia_declaracao(self.list_tokens[i+1])

            elif list_t[0] == '=':   
                self.busca(self.list_tokens[i-1])                
                c = i +1
                while self.list_tokens[c][1] != ';':
                    atribuicao += ""+ self.list_tokens[c][1] 
                    c+=1    

                self.atualiza(self.list_tokens[i-1], atribuicao)                                     
                                    
            elif list_t[1] == "/":  
                self.divisao_zero(self.list_tokens[i+1])
            elif list_t[0] == 'kid':
                self.busca(list_t)                                   
            i+=1 
        self.arquivo.close()
        return self.symbol_table

    #Verifica se a variavel existe
    def busca(self, valor):
          
        if self.symbol_table.get(valor[1]):
            return 1                                  
        else:
            print("Erro Semântico: variavel ´{0}´ nao declarada [linha {1}:coluna {2}]".format(valor[1], valor[2], valor[3]))
            sys.exit()

    #Método responsavel por verificar se já existe declarado  a variavel
    def verifica_existencia_declaracao(self, var):
       
        if self.symbol_table.get(var[1]):
            print("Erro Semântico: variavel ´{0}´ já declarada [linha {1}:coluna {2}]".format(var[1], var[2], var[3] ))
            sys.exit()
        else:
            self.inserir(var)

    #Inserir dados na tabela
    def inserir(self, token):        
        self.symbol_table[token[1]] = [token[0], 1, 0]
        self.reg_operacao(1, token[1], token[2])
    
    #Atualiza os valores de atribuição das variaveis
    def atualiza (self, val, atribuicao ):        
                                      
        lista_atualiza =  self.symbol_table[val[1]]               
        lista_atualiza[2] = self.busca_atribuicao(atribuicao)             
        self.symbol_table[val[1]]= lista_atualiza            
      
                                
        self.reg_operacao(2,val[1], atribuicao)

    #Busca as atribuições das variaveis
    def busca_atribuicao(self, valor):
        
        while (valor.isdigit() == False ):
            if( self.symbol_table.keys() != valor):
                return valor

            lista_atualiza = self.symbol_table[valor]
            valor = str(lista_atualiza[2])               
                
            #Se a atribuicao for um numero
            if valor.isdigit():                    
                return valor        
        return valor

    #Verifica se é uma divisão por zero
    def divisao_zero(self, valor):
        #se for dígito
        if valor[1].isdigit():
            if self.busca_atribuicao(valor[1]) == '0':
                print("Erro Semântico: divisão por zero não permitida [linha {0}:coluna {1}]".format(valor[2], valor[3]))            
                sys.exit()
        else:
            #se for variavel
            self.busca(valor)
            if self.busca_atribuicao(valor[1]) == '0' or self.symbol_table[valor[1]][2] == '0':
                print("Erro Semântico: divisão por zero não permitida [linha {0}:coluna {1}]".format(valor[2], valor[3]))            
                sys.exit()
            
    #registra as operações realizadas 
    def reg_operacao(self, val, variavel, valor = None):        
        if (val ==1):
           self.arquivo.write("Variavel {0} declarada\n".format(variavel))
           
        #para posterior verificação das atribuições em tempo de execução
        #elif (val == 2):
         #   self.arquivo.write("Variavel ´{0}´ atualizada o valor para ´{1}´\n".format(variavel, valor))
    
    #imprime o log que foi escrito anteriormente
    def log_operacoes(self):
        arquivo = open("log_operacao.txt","r")
        print("-=-"*20)
        print("\t\tLOG DE OPERACOES SEMANTICA")
        print("-=-"*20)
        for linha in arquivo:
            linha = linha.rstrip()
            print (linha)
        print('*'*50)
        arquivo.close()  