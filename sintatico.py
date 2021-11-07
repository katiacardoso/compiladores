import sys

class Analisador_Sintatico:

    def __init__(self, lista_tokens):
        #pilha sintatica iniciada com termo inicial da gramatica e $.
        self.pilha_sintatica = ['$', 'KINGUAGEM']
        #iniciando lista com a lista de tokens seguida de $.        
        self.list_tokens = list(lista_tokens)
        self.list_tokens.append('$')
        
        self.empilhamento = 0
        self.desempilhamento = 0
        self.reducao_pilha_lista = 0
        self.producoes_aplicadas = [ ]
        self.n_producoes_aplicadas= 0

        self.arquivo = open('log_operacao.txt','w')
        
        self.producoes = {
            0:  ["kinicio","CODIGO","kim"],
            1:  [],
            2:  ["INSTRUCAO",";","CODIGO"],
            3:  [],
            4:  ["VARIAVEIS"],
            5:  ["ESCREVA"],
            6:  ["LEIA"],
            7:  ["CONDICIONAL"],
            8:  ["REPETICAO"],
            9:  ["EXPRESSAO"],
            10: ["eskreva","(","EXPRESSAO" ,")"],
            11: ["leiak","(","kid",")"],
            12: ["SE","SENAO","fimsek"],
            13: ["sek","(","LOGICA",")","CODIGO"],
            14: ["senaok","CODIGO"],
            15: [],
            16: ["ENQUANTO","fimenkuanto"],
            17: ["enkuanto","(","LOGICA",")","CODIGO"],
            18: ["=","EXPRESSAO"],
            19: ["numeko"],
            20: [], 
            21: ["kint","kid","ATRIBUICAO"],
            22: ["kid","EXPRESSAO"],
            23: ["numeko","EXPRESSAO"],
            24: ["+","EXPRESSAO"],
            25: ["*","EXPRESSAO"],
            26: ["-","EXPRESSAO"],
            27: ["/","EXPRESSAO"],
            28: ["=","EXPRESSAO"],
            29: [],
            30: ["(","EXPRESSAO",")","EXPRESSAO"],
            31: ["KID_OU_NUMEKO","OPERADOR_LOGICO","KID_OU_NUMEKO"],
            32: ["kid"],
            33: ["numeko"],
            34: ["=="],
            35: ["<"]
        }
        
        self.nao_terminais = {
            'KINGUAGEM': [0,1],
            'CODIGO': [2, 3],
            'INSTRUCAO': [3, 4, 5, 6 , 7, 8,9],
            'ESCREVA' : [10],
            'LEIA': [11],
            'VARIAVEIS': [21],
            'CONDICIONAL': [12],
            'REPETICAO': [16],
            'EXPRESSAO': [22,23,24,25,26,27,28,29,30],
            'ENQUANTO': [17],
            'ATRIBUICAO': [18,19,20],
            'SE': [13],
            'SENAO': [14,15],
            'LOGICA': [31],
            'KID_OU_NUMEKO': [32,33],
            'OPERADOR_LOGICO': [34,35] 
        }
        
        self.terminais = {
            '$':[1],
            'numeko':[2,9,23,19,31,33],
            'kid': [2,9,22,31,32],
            'kint': [2, 4, 21],
            '(': [2,9,30],
            ')':[29],
            ';':[2,9,29,20],
            '=':[2,9,28,18],
            '+':[2,9,24],
            '-':[2,9,26],
            '*':[2,9,25],
            '/':[2,9,27],
            '==':[34],
            '<':[35],
            'kinicio':[0],
            'kim':[3],
            'sek':[2,7,12,13],
            'senaok': [3,14],
            'fimsek':[3,15],
            'enkuanto':[2,8,16,17],
            'fimenkuanto':[3],
            'eskreva':[2,5,10],
            'leiak':[2,6,11],
            'kint':[2,4,21]
        }
        
    def verificacao_sintatica(self):
        
        self.arquivo.write("EMPILHANDO: {0}  \n".format(self.pilha_sintatica[0]))
        self.arquivo.write("EMPILHANDO: {0} \n".format(self.pilha_sintatica[-1]))
        while ( self.list_tokens[0][0] != '$' and self.pilha_sintatica[-1] != '$' ):
            if self.list_tokens[0][0] == self.pilha_sintatica[-1]:
                self.reg_operacoes(3,-1)
                del self.list_tokens[0]  
                self.pilha_sintatica.pop()  
                self.reducao_pilha_lista += 1
                self.desempilhamento += 1     
                    
            elif len(self.list_tokens) == 0 and len(self.pilha_sintatica)>0:
                print("Errooou Sintático: Pilha sintática possui dados e lista sintática  está vazia [error performing parsing] ", self.pilha_sintatica )
                sys.exit()   
            elif len(self.list_tokens) > 0 and (self.pilha_sintatica) == 0:   
                print("Errooou Sintático: Lista sintática possui dados e pilha sintatica vazia [error performing parsing]", self.list_tokens)               
                sys.exit()
            else:
                self.tabela_sintatica()               
                 
        self.arquivo.write("DESEMPILHANDO:{0} \n".format(self.pilha_sintatica[-1]))
        self.arquivo.close()

     #Método para verificar regras de produção
    def tabela_sintatica(self):

        try:
            producao = self.verifica_producao() 
        except:
            print("Erro Sintático: não possível encontrar uma producao válida para o valor {0} na linha {1} e coluna {2}.[error performing parsing]".format(self.list_tokens[0][1], self.list_tokens[0][2], self.list_tokens[0][3]))
            sys.exit()
        else:
            self.aplica_producao(producao)

    #Metodo reponsavel por verificar se existe producao válida
    def verifica_producao (self):
        producao = []   
        x, y = self.valor_producao()            
        producao = list(set(x).intersection(y)) 
        return producao[0]
      
   
    #Método responsabel por retornar a chave dos dicionarios.
    def valor_producao(self):     
        key_stack  = [-1] 
        key_list = [-1]  
        #Procurando a chave correspondente da Pilha       
        for i in self.nao_terminais.keys():   
            if i == self.pilha_sintatica[-1]:                
                key_stack = self.nao_terminais[i]               
        #Procurando a chave correspondente da Lista.  
        for j in self.terminais.keys():  

            if j == self.list_tokens[0][0]:
                #print(self.terminais[j])
                key_list = self.terminais[j]

        return (key_stack,key_list)       
                    
    #Método responsavel por aplicar a producao
    def aplica_producao(self, producao):
        try:
            valor_producao = self.producoes[producao]
            self.producoes_aplicadas.append(producao)            
           
            self.reg_operacoes(1, producao)
            self.pilha_sintatica.pop()  
            self.desempilhamento += 1

            #producoes vazias
            if any([valor_producao != 1, valor_producao != 3, valor_producao != 15, valor_producao != 20, valor_producao != 29]):                     
                
                for i in reversed(valor_producao):                    
                    self.pilha_sintatica.append(i)
                    self.empilhamento += 1
                    self.reg_operacoes(2, producao)
              
        except:
            print("Erro Sintático: valor foi possivel encontrar uma producao valida para o valor  {0} na linha {1} e coluna {2}. [error performing parsing]".format(self.list_tokens[0][1], self.list_tokens[0][2], self.list_tokens[0][3]))            
         
    def reg_operacoes(self,n, producao):
    
        #operacoes de desempilhamento
        if n == 1:
            self.arquivo.write("DESEMPILHANDO:{0} ->  producao {1} inserida. \n".format(self.pilha_sintatica[-1], producao))
        #operacoes de empilhamento
        elif n == 2:
            self.arquivo.write("EMPILHANDO: {0} -> producao {1} aplicada. \n".format(self.pilha_sintatica[-1], producao))
        #reducao
        elif n ==3:  
            self.arquivo.write("REDUzindo: {0} \n".format(self.pilha_sintatica[-1],self.list_tokens[0][0] ))
       

    def log_operacoes (self):
        print("-=-"*20)
        print("\tLOG DE OPERACOES DO ANALISADOR SINTÁTICO")
        print("-=-"*20)

        arquivo = open("log_operacao.txt","r")
        for linha in arquivo:
            linha = linha.rstrip()
            print (linha)
        arquivo.close()