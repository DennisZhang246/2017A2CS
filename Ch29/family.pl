male(billy).
male(jimmy).
male(john).
male(jack).

female(mary).
female(elisabeth).
female(kris).

parent(bill,mary).
parent(kris,bill).
parent(jimmy,bill).
parent(elisabeth,mary).

/* rule */

brother(X,Y) :-
	male(X),
	male(Y),
	parent(Z,X),
	parent(Z,Y).

sister(X,Y) :-
	female(X),
	female(Y),
	parent(Z,X),
	parent(Z,Y).

son(X,Y) :-
	male(X),
	parent(X,Y).

daughter(X,Y) :-
	female(X),
	parent(X,Y).

married(X,Y) :-
	parent(X,Z),
	parent(Y,Z).

ancestor(X,Y) :-
	parent(X,Y);
	parent(X,Z),
	parent(Z,Y).

uncle(X,Y) :-
	male(Y),
	parent(X,Z),
	brother(Z,Y);
	sister(Z,Y).

aunt(X,Y) :-
	female(Y),
	parent(X,Z),
	brother(Z,Y);
	sister(Z,Y).




