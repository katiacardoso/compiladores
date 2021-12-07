import re
import os
import logging

class Codigo_Final:

    def __init__(self,cod_intermediario):
        self.codigo_final = []         
        self.variaveis = []
        self.addr_var = []
        self.cont_string = 0
        self.cont_label = 0
        self.label_se= 0 
        self.label_sek = 0
        self.label_senak = 0
        self.stack_label = []
        self.codigo_intermediario = []
        self.log_final = open("log_final.txt","w")
        self._arquivo = open(cod_intermediario, "r")

        
        for line in self._arquivo:
            self.codigo_intermediario.append(line)
        self._arquivo.close()

    def inicia_geracao(self, **asm_param):
        #definir um cabeçalho
        assembly_logger = logging.getLogger(__name__)
        assembly_logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        handler.setFormatter(logging.Formatter('%(message)s'))
        assembly_logger.addHandler(handler)
        assembly_logger.disabled = True

        if asm_param.get('vasm') is True or asm_param.get('vall') is True:
            file_handler = logging.FileHandler('log_final.txt', 'w+')
            file_handler.setFormatter(logging.Formatter('%(message)s'))
            assembly_logger.addHandler(file_handler)
            assembly_logger.disabled = False

        

        msg_counter = 1
        variable = []
        data = ['section .data', '\tformatin: db "%d",0', '\tformatout: db "%d",10,0']
        text = ['section .text', '\tglobal _main', '\textern _printf', '\textern _scanf']
        main = ['\t', '_main:']

        
        #começa a percorrer o arquivo
        for line in  self.codigo_intermediario:
            if 'kint' in line:
                assembly_logger.debug('\n\n\nStep: {}\t\t\t\tDetectado kint. Creating code for: {}'.format(line, line.split("kint")[1].strip()))
                self.log_final.write('\n\n\nStep: {}\t\t\t\tDetectado kint. Creating code for: {}'.format(line, line.split("kint")[1].strip()))

                data.append(f'\t{line.split("kint")[1].strip()}: dd 0')
                variable.append(line.split("kint")[1].strip())
            elif '=' in line:
                assembly_logger.debug('\n\n\n Step: {}\t\t Detectado aritmetica',format(line))
                self.log_final.write('\n\n\nStep: {}\t\t Detectado aritmetica')


                main.append('')

                if not line.split()[0].strip() in variable:
                    self.log_final('{} is not in variable list. Setting ZERO to it', line.split()[0].strip())
                    data.append(f'\t{line.split()[0].strip()}: dd 0')
                    variable.append(line.split()[0].strip())

                if '+' in line:
                    main.append(
                        f'mov eax, {"dword[" + line.split()[-3].strip() + "]" if not line.split()[-3].strip().isdecimal() else line.split()[-3].strip()}')
                    main.append(
                        f'mov ecx, {"dword[" + line.split()[-2].strip() + "]" if not line.split()[-2].strip().isdecimal() else line.split()[-2].strip()}')
                    main.append(f'add eax, ecx')
                    main.append(f'mov dword[{line.split()[0].strip()}], eax')
                
                elif '-' in line:
                    main.append(
                        f'mov eax, {"dword[" + line.split()[-3].strip() + "]" if not line.split()[-3].strip().isdecimal() else line.split()[-3].strip()}')
                    main.append(
                        f'mov ecx, {"dword[" + line.split()[-2].strip() + "]" if not line.split()[-2].strip().isdecimal() else line.split()[-2].strip()}')
                    main.append(f'sub eax, ecx')
                    main.append(f'mov dword[{line.split()[0].strip()}], eax')

                elif '*' in line:
                    main.append(
                        f'mov eax, {"dword[" + line.split()[-3].strip() + "]" if not line.split()[-3].strip().isdecimal() else line.split()[-3].strip()}')
                    main.append(
                        f'mov ecx, {"dword[" + line.split()[-2].strip() + "]" if not line.split()[-2].strip().isdecimal() else line.split()[-2].strip()}')
                    main.append(f'mul ecx')
                    main.append(f'mov dword[{line.split()[0].strip()}], eax')
                
                elif '/' in line:
                    main.append(
                        f'mov eax, {"dword[" + line.split()[-3].strip() + "]" if not line.split()[-3].strip().isdecimal() else line.split()[-3].strip()}')
                    main.append(
                        f'mov ecx, {"dword[" + line.split()[-2].strip() + "]" if not line.split()[-2].strip().isdecimal() else line.split()[-2].strip()}')
                    main.append(f'mov edx, 0')
                    main.append(f'div ecx')
                    main.append(f'mov dword[{line.split()[0].strip()}], eax')

                else:
                    #self.log_final.write('\n\n\nStep: {}\t\t depoois do else')
                    #main.append(f'mov dword[{line.split("=")[0].strip()}], {line.split("=")[1].strip()}')
                    main.append(f'mov edx, dword[{line.split("=")[1].strip()}]')   #mover outro numero
                    main.append(f'mov [{line.split("=")[0].strip()}], edx')
                    
            elif 'eskreva' in line.split()[0]:    
                assembly_logger.debug('\n\n\n Step: {}\t\tDetectado eskreva. Creating code for: {}'.format(line, line.split("eskreva")[1].strip()))
                self.log_final.write('\n\n\n Step: {}\t\tDetectado eskreva. Creating code for: {}'.format(line, line.split("eskreva")[1].strip()))
                if '"' in line.split("eskreva")[1]:
                    data.append(f'\tmgs{msg_counter}: db {line.split("eskreva")[1].strip()},10,0')
                    main.append('')
                    main.append(f'push mgs{msg_counter}')
                    main.append('call _printf')
                    main.append('add esp,4')
                    msg_counter += 1
                else:
                    
                    main.append('')
                    main.append(f'mov ebx, dword[{line.split("eskreva")[1].strip()}]')
                    main.append('push ebx')
                    main.append('push formatout')
                    main.append('call _printf')
                    main.append('add esp, 8')
            elif 'leiak' in line.split()[0]:
                assembly_logger.debug('\n\n\n Step: {}\t\tDetectado leiak. Creating code for: {}'.format(line, line.split("leiak")[1].strip()))
                self.log_final.write ('\n\n\n Step: {}\t\tDetectado leiak. Creating code for: {}'.format(line, line.split("leiak")[1].strip()))
                main.append('')
                main.append(f'push {line.split("leiak")[1].strip()}')
                main.append('push formatin')
                main.append('call _scanf')
                main.append('add esp,8')
            
            elif 'sek' in line.split()[0]:
                assembly_logger.debug('\n\n\n Step: {}\t\tDetectado sek. Creating statement...'.format(line))
                self.log_final.write('\n\n\n Step: {}\t\tDetectado sek. Creating statement...'.format(line))
                main.append('')
                main.append(f'mov eax,{ "dword[ {0}" +  "]"}'.format(line.split()[0].strip()))
                main.append(f'cmp eax,{ "dword[ {0}"  + "]"}'.format(line.split()[0].strip()))
            
                if '<' in line:
                    self.log_final.write('SEK Statement\t\tJumping JL to {}\n'.format(line.split()[5].strip()))
                    main.append(f'jl {line.split()[5].strip()}')

                elif '==' in line:            
                    self.log_final.write('SEK Statement\t\tJumping JE to {}\n'.format(line.split()[5].strip()))
                    main.append(f'je {line.split()[5].strip()}')

            elif 'enkuanto' in line.split()[0]:
                assembly_logger.debug('\n\n\n Step: {}\t\t enkuanto Statement --> Jumping JMP to {}\n'.format(line, line.split()[1].strip()))
                self.log_final.write('\n\n\n Step: {}\t\t enkuanto Statement --> Jumping JMP to {}\n'.format(line, line.split()[1].strip()))
                main.append('')
                main.append(f'jmp {line.split()[1].strip()}')            
            elif '_L' in line.split()[0]:
                assembly_logger.debug('\n\n\n Detectado Label {}\t\tCreating Statement'.format(line))
                self.log_final.write('\n\n\n  Detectado Label {}\t\tCreating Statement'.format(line))
                if 'sek' in line:
                    assembly_logger.debug('\n\n\n Step: {}\t\tDetected sek. Creating statement...'.format(line))
                    self.log_final.write('\n\n\n Step: {}\t\tDetected sek. Creating statement...'.format(line))
                    main.append('')
                    main.append(f'{line.split()[0]}')
                    main.append(
                        f'mov eax, {"dword[" + line.split()[2].strip() + "]" if not line.split()[2].strip().isdecimal() else line.split()[2].strip()}')
                    main.append(
                        f'cmp eax, {"dword[" + line.split()[4].strip() + "]" if not line.split()[4].strip().isdecimal() else line.split()[4].strip()}')
                    if '<' in line:
                        assembly_logger.debug('\n\n\n SEK Statement\t\tJumping JL to {}\n'.format(line.split()[6].strip()))
                        self.log_final.write('\n\n\n SEK Statement\t\tJumping JL to {}\n'.format(line.split()[6].strip()))
                        main.append(f'jl {line.split()[6].strip()}')


                    elif '==' in line:
                        assembly_logger.debug('\n\n\n IF Statement\t\tJumping JE to {}\n'.format(line.split()[6].strip()))
                        self.log_final.write('\n\n\n IF Statement\t\tJumping JE to {}\n'.format(line.split()[6].strip()))
                        main.append(f'je {line.split()[6].strip()}')

                else:
                    main.append('')
                    main.append(f'{line.strip()}')        
        
        code = data + text + main
        assembly_logger.debug('\n\n\n End of Program...\n\n\n')
        self.log_final.write('\n\n\n End of Program...\n\n\n')
        code.append('ret')
        self.log_final.close()
        self.getFinal(code)
       
        print("Final code generation performed successfully.")
    
    def getFinal(self,code):
        arquivo_final = open ("arquivo_saida.s","w")
        for line in code:            
            arquivo_final.write(line+"\n")
        arquivo_final.close() 

    def log_finalCode(self):
        log_f = open("log_final.txt","r")
        for log in log_f:
            print(log)
        log_f.close()