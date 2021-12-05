from infixa_posfixa import infix_to_postfix

class Intermediario:
    def __init__(self, list_tokens, list_id):
        self.lista_tokens = list_tokens
        self.lista_id = list(list_id.keys())
        self.cod_intermediario = []
        self.log_intermediario = open("log_intermediario.txt","w")

    def inicia_geracao(self):
        #Declarações de variaveis
        for id in self.lista_id:
           self.cod_intermediario.append('kint {0}'.format(id))
           self.log_intermediario.write("Declarado variavel {0}\n".format(id))
        #Gramática
        i=0
        for token in self.lista_tokens:

            if token[0] == 'leiak' :
               self.cod_intermediario.append("leiak {0}".format(self.lista_tokens[i+2][1]))
               self.log_intermediario.write("Comando de leitura da variavel {0} \n".format(self.lista_tokens[i+2][1])) 
            
            elif token[0] == 'eskreva':
                self.cod_intermediario.append("eskreva {0}".format(self.lista_tokens[i+2][1]))
                self.log_intermediario.write("Comando de escrita da variavel ou string {0}\n ".format(self.lista_tokens[i+2][1])) 


            elif token[0] == '=':
                j=i+1
                atribuicao =""
                while self.lista_tokens[j][0] != ';':
                    atribuicao += " "+self.lista_tokens[j][1]
                    j+=1
                  
                self.cod_intermediario.append("{0} = {1}".format(self.lista_tokens[i-1][1], infix_to_postfix(atribuicao)))     
                self.log_intermediario.write("Atribuido à {0} a expressão {1}\n ".format(self.lista_tokens[i-1][1], infix_to_postfix(atribuicao))) 

            elif token[0] == 'enkuanto':
                j=i+1                         
                condicao = " "
                exp = ""             
                    
                if self.lista_tokens[j][0] == "<":
                    condicao += infix_to_postfix(exp) + " "+self.lista_tokens[j][1]
                    exp = ""
                    j+=1

                else:
                    self.lista_tokens[j][0] == "=="
                    condicao += infix_to_postfix(exp) + " "+self.lista_tokens[j][1]
                    exp = ""
                    j+=1 

                exp += " "+self.lista_tokens[j][1]                        
                j+=1 
                            
                condicao += infix_to_postfix(exp) 
                self.cod_intermediario.append("enkuanto {0}".format(condicao))
                self.log_intermediario.write("Laço de repetição `enkuanto` reconhecido\n ") 
            
            elif token[0] == 'fimenkuanto':
                self.cod_intermediario.append("fimenkuanto")

            elif token[0] == 'sek':
                j=i+1                         
                condicao = " "
                exp = ""
                                   
                    
                if self.lista_tokens[j][0] == "<":
                    condicao += infix_to_postfix(exp) + " "+self.lista_tokens[j][1]
                    exp = ""
                    j+=1

                else:
                    self.lista_tokens[j][0] == "=="
                    condicao += infix_to_postfix(exp) + " "+self.lista_tokens[j][1]
                    exp = ""
                    j+=1 

                exp += " "+self.lista_tokens[j][1]                        
                j+=1 
                            
                condicao += infix_to_postfix(exp)              
         
                self.cod_intermediario.append("sek {0} entao".format(condicao))
                self.log_intermediario.write("Comando condicional `sek` reconhecido\n ") 

            elif token[0] == 'fimsek':
                self.cod_intermediario.append("fimsek")     

            elif token[0] == 'fimsek':
                self.cod_intermediario.append("senaok")
                self.log_intermediario.write("Comando condicional `senaok` reconhecido\n ") 


            i+=1
        
        self.log_intermediario.close()  
        self.getIntermediario() 
        return self.write_intermediario(self.cod_intermediario)
       
    def getIntermediario(self):
        arquivo_intermediario = open ("arquivo_intermediario.txt","w")
        for line in self.cod_intermediario:            
            arquivo_intermediario.write(line+"\n")
        arquivo_intermediario.close()    

    def write_intermediario(self, cod):
        intermediary = [str(a) for a in cod]
        return "\n".join(intermediary)

    def log_intermediary(self):
        log_int = open("log_intermediario.txt","r")
        for log in log_int:
            print(log)
        log_int.close()