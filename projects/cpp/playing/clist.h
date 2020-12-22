#ifndef CLIST_H
#define CLIST_H

#include<iostream>
#include"planet.h"

template<typename ltype>
struct link{

	// constructor	
	link();
	link(ltype input);

	// variables
	ltype elem;
	link<ltype>* forward;
	link<ltype>* backward;
};

template<typename type>
struct clist{

	// constructor 
	clist();

	
	// variables
	link<type>* init;
	link<type>* last;
	int n_elem;


	// overloads
	type& operator[](int);
	
	
	// methods
	void add(type);
	void del(int);
	int size();
	void print();
};

#endif
