section .data
	formatin: db "%d",0
	formatout: db "%d",10,0
	numero: dd 0
	fibonacci: dd 0
	auxiliar: dd 0
	mgs1: db "TESTANDO",10,0
	mgs2: db "digite o numero",10,0
	mgs3: db "maior que 5",10,0
section .text
	global _main
	extern _printf
	extern _scanf
	
_main:

push mgs1
call _printf
add esp,4

push mgs2
call _printf
add esp,4

push numero
push formatin
call _scanf
add esp,8

mov eax,dword[ sek]
cmp eax,dword[ sek]

push mgs3
call _printf
add esp,4

mov eax,dword[ fimsek]
cmp eax,dword[ fimsek]
ret
