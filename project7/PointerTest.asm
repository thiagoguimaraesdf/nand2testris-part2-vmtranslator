//push constant 3030
@3030
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop pointer 0
@3
D=A
@0
D=A+D
@SP
A=M
M=D
@SP
A=M-1
D=M
@SP
A=M
A=M
M=D
@SP
M=M-1
//push constant 3040
@3040
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop pointer 1
@3
D=A
@1
D=A+D
@SP
A=M
M=D
@SP
A=M-1
D=M
@SP
A=M
A=M
M=D
@SP
M=M-1
//push constant 32
@32
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop this 2
@2
D=A
@THIS
M=D+M
@SP
M=M-1
A=M
D=M
@THIS
A=M
M=D
A=M
@2
D=A
@THIS
M=M-D
//push constant 46
@46
D=A
@SP
A=M
M=D
@SP
M=M+1
//pop that 6
@6
D=A
@THAT
M=D+M
@SP
M=M-1
A=M
D=M
@THAT
A=M
M=D
A=M
@6
D=A
@THAT
M=M-D
//push pointer 0
@0
D=A
@3
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//push pointer 1
@1
D=A
@3
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
//add
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
//push this 2
@2
D=A
@THIS
A=D+M
D=M
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
//push that 6
@6
D=A
@THAT
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
//add
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
