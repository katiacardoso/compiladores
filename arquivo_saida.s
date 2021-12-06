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

mov dword[fibonacci], 0

mov dword[auxiliar], 0

push numero
push formatin
call _scanf
add esp,8

mov ebx, dword[numero]
push ebx
push formatout
call _printf
add esp, 8
ret
