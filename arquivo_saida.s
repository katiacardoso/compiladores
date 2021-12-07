section .data
	formatin: db "%d",0
	formatout: db "%d",10,0
	numero: dd 0
	mgs1: db "Codigo de fibonacci",10,0
section .text
	global _main
	extern _printf
	extern _scanf
	
_main:

push mgs1
call _printf
add esp,4

mov edx, dword[5]
mov [numero], edx

mov ebx, dword[numero]
push ebx
push formatout
call _printf
add esp, 8
ret
