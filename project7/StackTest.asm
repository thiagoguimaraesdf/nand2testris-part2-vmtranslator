//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//eq
@SP
AM=M-1
D=M
@SP
AM=M-1
D=D-M
@EQUAL3
D;JEQ
@SP
A=M
M=0
@SP
M=M+1
@CONTINUE3
0;JMP
(EQUAL3)
@SP
A=M
M=-1
@SP
M=M+1
(CONTINUE3)
//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
//eq
@SP
AM=M-1
D=M
@SP
AM=M-1
D=D-M
@EQUAL6
D;JEQ
@SP
A=M
M=0
@SP
M=M+1
@CONTINUE6
0;JMP
(EQUAL6)
@SP
A=M
M=-1
@SP
M=M+1
(CONTINUE6)
//push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1
//eq
@SP
AM=M-1
D=M
@SP
AM=M-1
D=D-M
@EQUAL9
D;JEQ
@SP
A=M
M=0
@SP
M=M+1
@CONTINUE9
0;JMP
(EQUAL9)
@SP
A=M
M=-1
@SP
M=M+1
(CONTINUE9)
//push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//lt
@SP
AM=M-1
D=M
@SP
AM=M-1
D=D-M
@GREATER12
D;JGT
@SP
A=M
M=0
@SP
M=M+1
@CONTINUE12
0;JMP
(GREATER12)
@SP
A=M
M=-1
@SP
M=M+1
(CONTINUE12)
//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1
//lt
@SP
AM=M-1
D=M
@SP
AM=M-1
D=D-M
@GREATER15
D;JGT
@SP
A=M
M=0
@SP
M=M+1
@CONTINUE15
0;JMP
(GREATER15)
@SP
A=M
M=-1
@SP
M=M+1
(CONTINUE15)
//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1
//lt
@SP
AM=M-1
D=M
@SP
AM=M-1
D=D-M
@GREATER18
D;JGT
@SP
A=M
M=0
@SP
M=M+1
@CONTINUE18
0;JMP
(GREATER18)
@SP
A=M
M=-1
@SP
M=M+1
(CONTINUE18)
//push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt
@SP
AM=M-1
D=M
@SP
AM=M-1
D=D-M
@LESS21
D;JLT
@SP
A=M
M=0
@SP
M=M+1
@CONTINUE21
0;JMP
(LESS21)
@SP
A=M
M=-1
@SP
M=M+1
(CONTINUE21)
//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt
@SP
AM=M-1
D=M
@SP
AM=M-1
D=D-M
@LESS24
D;JLT
@SP
A=M
M=0
@SP
M=M+1
@CONTINUE24
0;JMP
(LESS24)
@SP
A=M
M=-1
@SP
M=M+1
(CONTINUE24)
//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1
//gt
@SP
AM=M-1
D=M
@SP
AM=M-1
D=D-M
@LESS27
D;JLT
@SP
A=M
M=0
@SP
M=M+1
@CONTINUE27
0;JMP
(LESS27)
@SP
A=M
M=-1
@SP
M=M+1
(CONTINUE27)
//push constant 57
@57
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1
//push constant 53
@53
D=A
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
//push constant 112
@112
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
//neg
@SP
A=M-1
M=-M
@SP
A=M
M=M-1
//and
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M&D
@SP
M=M+1
//push constant 82
@82
D=A
@SP
A=M
M=D
@SP
M=M+1
//or
@SP
AM=M-1
D=M
@SP
AM=M-1
M=M|D
@SP
M=M+1
//not
@SP
A=M-1
M=!M
@SP
A=M
M=M-1
