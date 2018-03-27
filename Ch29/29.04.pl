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

ancestor(X,Y) :-
	parent(X,Y);
	parent(X,Z),
	parent(Z,Y).