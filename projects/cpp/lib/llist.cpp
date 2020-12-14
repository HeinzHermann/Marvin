#include<iostream>


template <typename T>
void t_print(T var){
	std::cout << "We are now printing the type " << typeid(var).name() <<
			" and the variable var = " << var << std::endl;
}	


struct link{
	
	// variables
	int numb = 0;
	link* forward = NULL;
	link* backward = NULL;
};

struct llist{
	link* init = new link;
	link* last = init;
	int n_elem = 1;

	
	// overloads
	int& operator[](int x){
		link* nextp = init;
		for(int i=0; i<x; i++){
			nextp = nextp->forward;	
		}
		return nextp->numb;
	}
	
	
	// methods
	void add(int new_int){
		//do stuff
		link* next;
	        next = new link;
		next->numb = new_int;
		last->forward = next;
		next->backward = last;
		last = next;
		n_elem++;
	}

	void del(int pos){
		// navigate to del item
		link* current = init;
		for(int i=0; i<pos; i++){
			current = current->forward;
		}

		// add case where only init element exists
		if ((current->backward != NULL) and (current->forward != NULL)) {
			// move forwad p of pref elem to next elem
			current->backward->forward = current->forward;
			// move backward p of next elem to prev elem
			current->forward->backward = current->backward;
			// delete elemt
			free(current);
		} else if((current->backward != NULL) and (current->forward == NULL)) {
			// set forward p of pref elem to NULL
			current->backward->forward = NULL;
			// set last elem to new end
			this->last = current->backward;
			// delete last elemt
			free(current);
		} else if((current->backward == NULL) and (current->forward != NULL)) {
			// set backward p of next elem to NULL
			current->forward->backward = NULL;
			// set new initial element
			this->init = current->forward;
			// delete first elem
			free(current);
		}
		n_elem--;
	}
	
	// print entire linked list
	void print(){
		link* current = init;
		std::cout << "[ ";
		for(int i=0; i<n_elem; i++){
			std::cout << current->numb << " ";
			current = current->forward;	
		}
		std::cout << "]" << std::endl;

	}
	
};


int main(int argc, char* argv[]){
	
	llist inta;
	inta[0] = 8;
	inta.add(5);
	inta.add(3);
	inta.add(1);
	printf("added numbers 5,3,1 and set inta[0] to 8\n");
	inta.print();
	inta[2]=77;
	inta.del(1);
	printf("set inta[2] to 77 and deleted element 1\n");
	inta.print();
	inta.del(0);
	printf("delete first elem\n");
	inta.print();
	inta.del(1);
	printf("delete last elem\n");
	inta.print();
	return 0;
}
