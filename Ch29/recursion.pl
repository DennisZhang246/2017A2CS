factorial(O,1).
factorial(N,F) :-
	M is N - 1,
	factorial(M,X), 
	F is X * N.

buuunyears(0,0).
bunnyears(N,F) :-
	M is N - 1
	bunnyears(M,X),
	F is X + 2.

fibonacci(0,0).
fibonacci(1,1).
fibonacci(N,F) :-
	M is N - 1,
	fibonacci(M,X),
	P is N - 2,
	fibonacci(P,Y),
	F is X + Y.

bunnyears2(0,0).
bunnyears2(N,F) :-
    M is N - 1,
    bunnyears2(M,X),
    N is L mod 2,
    Y is N+2+M.

triangle(0,0).
triangle(1,1).
triangle(N,F).
	M is N - 1,
	triangle(M,X),
	F is X + N.

sumdigit(0,0).
sumdigit(N,F) :-
	M is N div 10
	sumdigit(M,X),
	L is N mod 10
	sumdigit(L,Y),
	F is X + Y.

count7(0,0).
count7(N,F):- 
    M is N//10,
    L is N mod 10,
    count7(M, X),
    F is X+ L // 7 - L // 8.




