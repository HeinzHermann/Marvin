#include<iostream>

template<typename ltype>
struct link{
	// variables
	ltype elem;
	link<ltype>* forward = NULL;
	link<ltype>* backward = NULL;
};

template<typename type>
struct clist{
	link<type>* init = NULL;
	link<type>* last = NULL;
	int n_elem = 0;

	// overloads
	// weird code, how to make work?
	type& operator[](int x){
		link<type>* nextp = init;
		for(int i=0; i<x; i++){
			nextp = nextp->forward;	
		}
		return nextp->elem;
	}
	
	
	// methods
	void add(type nelem){
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

	void del(int pos){
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
	
	// print entire linked list
	void print(){
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
};


int main(int argc, char* argv[]){

	#define integer
	//#define character
	//#define floater

	
	#ifdef integer
	printf("initialized clist\n");
	clist<int> inta;
	inta.print();

	inta.add(8);
	inta.add(5);
	inta.add(3);
	inta.add(1);
	printf("added elements 8,5,3,1\n");
	inta.print();

	printf("set inta[2] to 77\n");
	inta[2]=77;
	inta.print();
	#endif

	#ifdef character
	printf("initialized clist\n");
	clist<char> inta;
	inta.print();

	inta.add('a');
	inta.add('b');
	inta.add('c');
	inta.add('d');
	printf("added elements a,b,c,d\n");
	inta.print();

	printf("set inta[2] to x\n");
	inta[2]='x';
	inta.print();
	#endif

	#ifdef floater
	printf("initialized clist\n");
	clist<float> inta;
	inta.print();

	inta.add(1.3);
	inta.add(2.0);
	inta.add(3.75833);
	inta.add(4.4);
	printf("added elements 1.3,2.0,3.75833,4.4\n");
	inta.print();

	printf("set inta[2] to 88\n");
	inta[2]=88;
	inta.print();
	#endif

	printf("deleted element 1\n");
	inta.del(1);
	inta.print();

	printf("delete first elem\n");
	inta.del(0);
	inta.print();

	printf("delete last elem\n");
	inta.del(1);
	inta.print();

	printf("delete final elem\n");
	inta.del(0);
	inta.print();

	printf("try to delete non existing element\n");
	inta.del(1);
	inta.print();
	return 0;
}
