;10.Z = (XY + 1)/ X^2;
;11.Z = (X+Y)/(X-Y);
;12.Z = - 1/X^3 + 3;
;13.Z = X - Y/X +1;
;14.Z = ((X+Y)/Y^2 - 1)*X;
;10 - символ переноса строки
format PE console

entry start

include 'win32a.inc'

section '.data' data readable writable
        example10 db 'Example 10. (XY + 1) / X^2 =',0
        example11 db 'Example 11. (X + Y) / (X - Y) =', 0
        example12 db 'Example 12. -1 / X^3 + 3 =', 0
        example13 db 'Example 13. X - Y / X + 1 =', 0
        example14 db 'Example 14. ((X + Y)/Y^2 - 1) * X =', 0

        inputX db 'Input X: ', 0
        inputY db 'Input Y: ', 0

        result db 'Result: %d', 10, 0
        inf db 'infinity', 0
        spaceStr db ' %d', 0

        X dd ?
        Y dd ?
        tmpX dd ?
        tmpY dd ?

        NULL = 0

section '.code' code readable executable
        start:
                push inputX
                call [printf]

                push X
                push spaceStr
                call [scanf]

                push inputY
                call [printf]

                push Y
                push spaceStr
                call [scanf]

                task10:
                mov eax, [X]
                add eax, [Y]

                mov ecx, [X]
                sub ecx, [Y]
                mov edx, 0

                div ecx

                push eax
                push result
                call [printf]

                push ecx
                push result
                call [printf]

                finish:
                call[getch]
                push NULL
                call [ExitProcess]

                print:
                mov eax, [X]
                push eax
                push result
                call [printf]

                jmp finish


section '.idata' import data readable
        library kernel, 'kernel32.dll', \
                msvcrt, 'msvcrt.dll'

        import kernel, \
               ExitProcess, 'ExitProcess'

        import msvcrt, \
               printf, 'printf', \
               scanf, 'scanf', \
               getch, '_getch'