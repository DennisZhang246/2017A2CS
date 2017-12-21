{\rtf1\ansi\ansicpg936\cocoartf1504\cocoasubrtf830
{\fonttbl\f0\fnil\fcharset204 PTSans-Regular;\f1\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;\red109\green109\blue109;\red251\green251\blue251;\red72\green72\blue72;
\red109\green109\blue109;\red39\green39\blue39;}
{\*\expandedcolortbl;;\cssrgb\c50196\c50196\c50196\c40000;\cssrgb\c98824\c98824\c98824;\cssrgb\c35294\c35294\c35294;
\cssrgb\c50196\c50196\c50196\c60000;\cssrgb\c20392\c20392\c20392;}
\paperw11900\paperh16840\margl1440\margr1440\vieww10800\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs57\fsmilli28900 \cf2 \cb3 \expnd0\expndtw0\kerning0
#
\b \cf4  
\i\b0 \cf5 _
\b \cf4 Task 25.02
\b0 \cf5 _
\i0\b \cf4  Dry Run
\b0\fs34 \
\pard\pardeftab720\partightenfactor0

\fs47\fsmilli23800 \cf2 ##
\b \cf4  S3C3 Dennis
\b0\fs34 \
\
\pard\pardeftab720\partightenfactor0

\f1\fs30\fsmilli15300 \cf4 Call Varible | Procedure call | n=0 | n=1 | Result | Return Value |\
--- | --- | --- | --- | ---\
1 | x(19) | False | False | x(9) |  \
2 | x(9) | False | False | x(4) |\
3 | x(4) | False | False | x(2) |\
4 | x(2) | False | False | x(1) |\
5 | x(1) | False | True |  | 1\
(4) | x(2) |  |  | 0 | 0\
(3) | x(4) |  |  | 0 | 0\
(2) | x(9) |  |  | 1 | 1\
(1) | x(19) |  |  | 1 | 1\
\
\pard\pardeftab720\partightenfactor0

\f0\fs34 \cf4 \
\pard\pardeftab720\partightenfactor0

\fs47\fsmilli23800 \cf2 ##
\b \cf4 Ch25 End of Chapter Questions
\b0\fs34 \
\pard\pardeftab720\partightenfactor0

\fs40\fsmilli20400 \cf2 ###
\b \cf4 S3C3 Dennis
\b0\fs34 \
\
\pard\pardeftab720\partightenfactor0

\fs37\fsmilli18700 \cf2 ####
\b \cf5 **\cf4 1(a)\cf5 **
\b0\fs34 \cf4 \

\fs37\fsmilli18700 \cf2 ####
\b \cf4 Iteration will repeat one program in the times it is asked to repeat. Recursion is self-referencing itself in one function.
\b0\fs34 \
\

\fs37\fsmilli18700 \cf2 ####
\b \cf5 **\cf4 1(b)\cf5 **
\b0\fs34 \cf4 \

\fs37\fsmilli18700 \cf2 ####
\b \cf4 Recursive is much briefer but takes more storage space.
\b0\fs34 \
\

\fs37\fsmilli18700 \cf2 ####
\b \cf5 **\cf4 2(a)\cf5 **
\b0\fs34 \cf4 \

\fs37\fsmilli18700 \cf2 ####
\b \cf4 Recursively define means in it call itself in its own funtion.
\b0\fs34 \
\

\fs37\fsmilli18700 \cf2 ####
\b \cf5 **\cf4 2(b)\cf5 **
\b0\fs34 \cf4 \
\pard\pardeftab720\partightenfactor0

\f1\fs30\fsmilli15300 \cf4 Call number|Procedure call|Exponent = 0|Result\
---|---|---|---\
1|Power(2,4)|False|2*Power(2,3)\
2|Power(2,3)|False|2\cf5 *\cf4 2\cf5 *\cf4 Power(2,2)\
3|Power(2,2)|False|2\cf5 *\cf4 2\cf5 *\cf4 2*Power(2,1)\
4|Power(2,1)|False|2\cf5 *\cf4 2\cf5 *\cf4 2\cf5 *\cf4 2\cf5 *\cf4 Power(2,0)\
5|Power(2,0)|True|2\cf5 *\cf4 2\cf5 *\cf4 2\cf5 *\cf4 2\cf5 *\cf4 1\
(4)|Power(2,1)|False|2\
(3)|Power(2,2)|False|4\
(2)|Power(2,3)|False|8\
(1)|Power(2,4)|False|16\
\
\pard\pardeftab720\partightenfactor0

\f0\fs37\fsmilli18700 \cf2 ####
\b \cf5 **\cf4 2(c)\cf5 **
\b0\fs34 \cf4 \

\fs37\fsmilli18700 \cf2 ####
\b \cf4 The result of first called procedure will be lastly returned, and vice versa.
\b0\fs34 \
\

\fs37\fsmilli18700 \cf2 ####
\b \cf5 **\cf4 2(e)\cf5 **
\b0\fs34 \cf4 \
\pard\pardeftab720\partightenfactor0

\f1\fs30\fsmilli15300 \cf5 ```\cf6 pseudocode\
FUNCTION Power(Base : INTEGER, Exponent : INTEGER) RETURNS INTEGER\
Result = 1\
WHILE Exponent > 0\
	Result = Result * Base\
	Exponent = Exponent - 1 \
ENDWHILE\
RETURN Result\
ENDFUNCTION\
\cf5 ```
\f0\fs34 \cf4 \
\pard\pardeftab720\partightenfactor0

\fs37\fsmilli18700 \cf2 ####
\b \cf5 **\cf4 2(f)\cf5 **
\b0\fs34 \cf4 \
\pard\pardeftab720\partightenfactor0

\b \cf5 **\cf4 i\cf5 **
\b0 \cf4 \
\pard\pardeftab720\partightenfactor0

\fs37\fsmilli18700 \cf2 ####
\b \cf4 Iteration takes less storage area.
\b0\fs34 \
\pard\pardeftab720\partightenfactor0

\b \cf5 **\cf4 ii\cf5 **
\b0 \cf4 \
\pard\pardeftab720\partightenfactor0

\fs37\fsmilli18700 \cf2 ####
\b \cf4 Recursion is briefer.
\b0\fs34 \
\

\fs37\fsmilli18700 \cf2 ####
\b \cf5 **\cf4 3(a)\cf5 **
\b0\fs34 \cf4 \

\fs37\fsmilli18700 \cf2 ####
\b \cf5 **\cf4 i\cf5 **\cf4 		Line 04
\b0\fs34 \

\fs37\fsmilli18700 \cf2 ####
\b \cf5 **\cf4 ii\cf5 **\cf4 		Line 06
\b0\fs34 \
\

\fs37\fsmilli18700 \cf2 ####
\b \cf5 **\cf4 3(b)\cf5 **
\b0\fs34 \cf4 \
\pard\pardeftab720\partightenfactor0

\f1\fs30\fsmilli15300 \cf4 Call Varible | Procedure call | (Result=1) or (Result=0)| Result | Return Value |\
--- | --- | --- | --- | ---\
1 | Fibonacci(4) | False | Fibonacci(3) |  \
2 | Fibonacci(3) | False | Fibonacci(2) |  \
3 | Fibonacci(2) | False | Fibonacci(1) |  \
4 | Fibonacci(1) | True | Fibonacci(0) | 1\
5 | Fibonacci(0) | True | 1 | 1\
6 | Fibonacci(2) | False | Fibonacci(1) |  \
7 | Fibonacci(1) | True | Fibonacci(0) | 1\
(3) |  | True |  | 1\
8 | Fibonacci(0) | True | 1 | 1\
(7) |  |  | 2 | 1\
(1) |  |  | 0 | 1 \
\
\pard\pardeftab720\partightenfactor0

\f0\fs34 \cf4 \
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
\
}