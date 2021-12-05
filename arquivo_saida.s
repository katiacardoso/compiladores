section .data
	formatin: db "%d",0
	formatout: db "%d",10,0
	numero: dd 0
	fibonacci: dd 0
	auxiliar: dd 0
section .text
	global _main
	extern _printf
	extern _scanf
	
_main:

mov dword[numero], 5

mov dword[fibonacci], 0

mov dword[auxiliar], 0

mov eax,dword[ sek]
cmp eax,dword[ sek]

mov ebx, dword[numero]
push ebx
push formatout
call _printf
add esp, 8

mov eax, dword[fibonacci]
mov ecx, dword[auxiliar]
add eax, ecx
mov dword[fibonacci], eax

mov dword[auxiliar], numero

mov dword[numero], fibonacci

mov eax,dword[ fimsek]
cmp eax,dword[ fimsek]
ret
