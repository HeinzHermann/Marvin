#include<iostream>
#include "clist.h"

// link struct
template <typename T>
link<T>::link(){
	forward = NULL;
	backward = NULL;
}

template <typename T>
link<T>::link(T inp){
	elem = inp;
	forward = NULL;
	backward = NULL;
}


// clist struct
template <typename type>
clist<type>::clist(){
	init = NULL;
	last = NULL;
	n_elem = 0;
}

template <typename type>
type& clist<type>::operator[](int x){
	link<type>* nextp = init;
	for(int i=0; i<x; i++){
		nextp = nextp->forward;	
	}
	return nextp->elem;
}

template <typename type>
void clist<type>::add(type nelem){
	link<type>* next;
        next = new link<type>;
	next->elem = nelem;
	
	if(n_elem == 0){
		this->init = next;
		this->last = next;
	} else {
		last->forward = next;
		next->backward = last;
		this->last = next;
	}
	n_elem++;
}

template <typename type>
void clist<type>::del(int pos){
	// only delete if elements exits and pos exists
	if(this->n_elem != 0 && pos <= this->n_elem && pos >= 0){
		
		// navigate to del item
		link<type>* current = init;
		for(int i=0; i<pos; i++){
			current = current->forward;
		}

		// neither first nor last element
		if ((current->backward != NULL) and (current->forward != NULL)) {
			current->backward->forward = current->forward;
			current->forward->backward = current->backward;
			delete current;
		// last element
		} else if((current->backward != NULL) and (current->forward == NULL)) {
			// set forward p of pref elem to NULL
			current->backward->forward = NULL;
			// set last elem to new end
			this->last = current->backward;
			// delete last elemt
			delete current;
		// first element
		} else if((current->backward == NULL) and (current->forward != NULL)) {
			// set backward p of next elem to NULL
			current->forward->backward = NULL;
			// set new initial element
			this->init = current->forward;
			// delete first elem
			delete current;
		// only one element exists
		} else {
			this->init = NULL;
			this->last = NULL;
			delete current;
		}
		n_elem--;
	}
}


template <typename type>
void clist<type>::print(){
	link<type>* current = init;
	std::cout << "[";
	if(this->n_elem != 0){
		std::cout << current->elem;
		for(int i=1; i<n_elem; i++){
			current = current->forward;	
			std::cout << ", " << current->elem;
		}
	}
	std::cout << "]" << std::endl;

}

template <typename type>
int clist<type>::size(){
	return n_elem;
}

