@256
D=A
@SP
M=D
@RETURN_ADDR0
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@5
D=D-A
@0
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(RETURN_ADDR0)
//function Main.fibonacci 0
(Main.fibonacci)
//push argument 0
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
//push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
//lt                     // checks if n<2
@SP
AM=M-1
D=M
@SP
AM=M-1
D=D-M
@GREATER4
D;JGT
@SP
A=M
M=0
@SP
M=M+1
@CONTINUE4
0;JMP
(GREATER4)
@SP
A=M
M=-1
@SP
M=M+1
(CONTINUE4)
//if-goto IF_TRUE
@SP
AM=M-1
D=M
@IF_TRUE
D;JNE
//goto IF_FALSE
@IF_FALSE
0;JMP
//label IF_TRUE          // if n<2, return n
(IF_TRUE)
//push argument 0        
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
//return
@LCL
D=M
@R11
M=D
@5
A=D-A
D=M
@R12
M=D
@0
D=A
@ARG
M=D+M
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
A=M
@0
D=A
@ARG
M=M-D
@ARG
D=M
@SP
M=D+1
@R11
D=M-1
AM=D
D=M
@THAT
M=D
@R11
D=M-1
AM=D
D=M
@THIS
M=D
@R11
D=M-1
AM=D
D=M
@ARG
M=D
@R11
D=M-1
AM=D
D=M
@LCL
M=D
@R12
A=M
0;JMP
//label IF_FALSE         // if n>=2, returns fib(n-2)+fib(n-1)
(IF_FALSE)
//push argument 0
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
//push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
//sub
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M-D
@SP
M=M+1
//call Main.fibonacci 1  // computes fib(n-2)
@RETURN_ADDR1
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(RETURN_ADDR1)
//push argument 0
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
//push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
//sub
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M-D
@SP
M=M+1
//call Main.fibonacci 1  // computes fib(n-1)
@RETURN_ADDR2
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(RETURN_ADDR2)
//add                    // returns fib(n-1) + fib(n-2)
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
M=M+D
@SP
M=M+1
//return
@LCL
D=M
@R11
M=D
@5
A=D-A
D=M
@R12
M=D
@0
D=A
@ARG
M=D+M
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
A=M
@0
D=A
@ARG
M=M-D
@ARG
D=M
@SP
M=D+1
@R11
D=M-1
AM=D
D=M
@THAT
M=D
@R11
D=M-1
AM=D
D=M
@THIS
M=D
@R11
D=M-1
AM=D
D=M
@ARG
M=D
@R11
D=M-1
AM=D
D=M
@LCL
M=D
@R12
A=M
0;JMP
//function Sys.init 0
(Sys.init)
//push constant 4
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
//call Main.fibonacci 1   // computes the 4'th fibonacci element
@RETURN_ADDR3
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@5
D=D-A
@1
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Main.fibonacci
0;JMP
(RETURN_ADDR3)
//label WHILE
(WHILE)
//goto WHILE              // loops infinitely
@WHILE
0;JMP